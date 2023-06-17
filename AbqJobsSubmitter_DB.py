#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Yinsong Li 
Date: 2023.06.16
"""

from PyQt5.QtWidgets import (QWidget, QApplication, QFileDialog, QMessageBox)
from PyQt5.QtCore import QThread, pyqtSignal
import sys, subprocess, os

from AbqJobsSubmitter_UI import Ui_AbqJobsSubmitter

class AbqJobThread(QThread):
    cur_job_id = pyqtSignal(int)
    complete = pyqtSignal()
    
    def __init__(self, abq_cmd_list:list, abq_wd_str:str):
        super(AbqJobThread, self).__init__()
        self.abq_cmd_list = abq_cmd_list
        self.abq_wd = abq_wd_str
    
    def run(self):
        for idx, cmd in enumerate(self.abq_cmd_list):
            print(idx, cmd)
            self.cur_job_id.emit(idx+1)
            subprocess.Popen(cmd, shell=True, cwd=self.abq_wd,
                            stdout=None, stderr=None).wait()
        self.complete.emit()


class SubmitterWindow(QWidget, Ui_AbqJobsSubmitter):
    
    def __init__(self):
        super(SubmitterWindow, self).__init__()
        
        self.cur_dir = ''
        self.last_dir = ''
        self.cmd_str_list = []
        self.abq_ver = 'abaqus'
        self.cpus_num = 8
        self.isDeleteFiles = True
        self.del_expect_fileTypeSet = {'inp', 'odb'}
        
        self.abq_jobs = None

        self.setupUi(self)
        self.lineEdit_InputFolder.setStyleSheet('color: #828282')
        self.lineEdit_AbqVer.setEnabled(False)

    def handleEditInpFolder(self):
        self.cur_dir = self.lineEdit_InputFolder.text()
        # print(self.cur_dir)
        return 
    
    def handleSelectInpFolder(self):
        if self.last_dir:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", self.last_dir)
        else:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "./")
        self.cur_dir = folder_path
        if self.cur_dir:
            self.last_dir = self.cur_dir
            self.lineEdit_InputFolder.setText(self.cur_dir)
        return 
    
    def handleEditAbqVer(self):
        self.abq_ver = self.lineEdit_AbqVer.Text()
        return 
      
    def handleEditCPUnums(self, cpus_num):
        self.cpus_num = cpus_num
        print(self.cpus_num)
        return 
    
    def handleToggleDeleteFiles(self, isDelete):
        self.isDeleteFiles = isDelete
        self.checkBox_DAT.setEnabled(isDelete)
        self.checkBox_LOG.setEnabled(isDelete)
        self.checkBox_MSG.setEnabled(isDelete)
        self.checkBox_RES.setEnabled(isDelete)
        self.checkBox_STA.setEnabled(isDelete)
        self.checkBox_STT.setEnabled(isDelete)
        return 
    
    def handleToggleFileType_STA(self, isSTAexpect):
        if isSTAexpect:
            self.del_expect_fileTypeSet.add('sta')
        else:
            self.del_expect_fileTypeSet.remove('sta')
        return 
    
    def handleToggleFileType_LOG(self, isLOGexpect):
        if isLOGexpect:
            self.del_expect_fileTypeSet.add('log')
        else:
            self.del_expect_fileTypeSet.remove('log')
        return 
    
    def handleToggleFileType_MSG(self, isMSGexpect):
        if isMSGexpect:
            self.del_expect_fileTypeSet.add('msg')
        else:
            self.del_expect_fileTypeSet.remove('msg')
        return 
    
    def handleToggleFileType_DAT(self, isDATexpect):
        if isDATexpect:
            self.del_expect_fileTypeSet.add('dat')
        else:
            self.del_expect_fileTypeSet.remove('dat')
        return 
    
    def handleToggleFileType_RES(self, isRESexpect):
        if isRESexpect:
            self.del_expect_fileTypeSet.add('res')
        else:
            self.del_expect_fileTypeSet.remove('res')
        return 
    
    def handleToggleFileType_STT(self, isSTTexpect):
        if isSTTexpect:
            self.del_expect_fileTypeSet.add('stt')
        else:
            self.del_expect_fileTypeSet.remove('stt')
        return 
    
    def handleSubmit(self):
        inps_list = self.get_inp_list(self.cur_dir)
        for job in inps_list:
            cmd = "{0} job={1} cpus={2} int ask=off".format(self.abq_ver, job, self.cpus_num)
            self.cmd_str_list.append(cmd)
        self.pushButton_Submit.setEnabled(False)
        self.excute_jobs_thread()
    
    def get_inp_list(self, folder_dir):
        inps_ls = []
        try:
            file_ls = os.listdir(folder_dir)
            for file in file_ls:            
                (filename, suffix) = os.path.splitext(file)
                if suffix == '.inp':
                    inps_ls.append(filename)
        except FileNotFoundError:
            QMessageBox.critical(self, 'Error: File Not Found',
                    'The directory is invalid, Please reselect!')
        return inps_ls
    
    def excute_jobs_thread(self):
        self.abq_jobs = AbqJobThread(self.cmd_str_list, self.cur_dir)
        self.abq_jobs.cur_job_id.connect(self.updateState)
        self.abq_jobs.complete.connect(self.handleComplete)
        self.abq_jobs.start()
            
    def updateState(self, current:int):
        total_jobs_num = len(self.cmd_str_list)
        self.setWindowTitle('AbqJobSubmitter-Current/Total: {0}/{1}'.format(current, total_jobs_num))
        
    def handleComplete(self):
        self.pushButton_Submit.setEnabled(True)
        inps_list = self.get_inp_list(self.cur_dir)
        if self.isDeleteFiles:
            self.setWindowTitle('AbqJobSubmitter-Deleting')
            self.deletefiles(self.cur_dir , inps_list, self.del_expect_fileTypeSet)
        self.setWindowTitle('AbqJobSubmitter-Complete!')
            
    def deletefiles(self, file_path, inp_file_list, expect_file_type={'inp', 'odb'}):
        file_ls = os.listdir(file_path)
        for file in file_ls:
            f_path = os.path.join(file_path, file)
            if os.path.isdir(f_path):
                continue
            elif not file.split(".")[0] in inp_file_list:
                continue
            elif file.split(".")[-1] in expect_file_type:
                continue
            else:
                os.remove(f_path)
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = SubmitterWindow()
    ex.show()
    sys.exit(app.exec_())