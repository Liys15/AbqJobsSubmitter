#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Yinsong Li 
Date: 2023.06.16
"""

from PyQt5.QtWidgets import (QWidget, QApplication, QFileDialog, QMessageBox)
import sys, subprocess, os

from AbqJobsSubmitter_UI import Ui_AbqJobsSubmitter


def run_cmd_Popen_fileno(cmd_string, file_path):
    return subprocess.Popen(cmd_string, shell=True, cwd=file_path,
                            stdout=None, stderr=None).wait()

class SubmitterWindow(QWidget, Ui_AbqJobsSubmitter):

    def __init__(self):
        super(SubmitterWindow, self).__init__()
        
        self.inps_folder_dir = ''
        self.last_dir = ''
        self.inps_list = []
        self.abaqus_ver_cmd = 'abaqus'
        self.cpus_num = 8
        self.isDeleteFiles = True
        self.del_expect_fileTypeList = set()
        
        self.setupUi(self)
        self.lineEdit_InputFolder.setStyleSheet('color: #828282')
        self.lineEdit_AbqVer.setEnabled(False)

    def handleEditInpFolder(self):
        self.inps_folder_dir = self.lineEdit_InputFolder.text()
        # print(self.inps_folder_dir)
        return 
    
    def handleSelectInpFolder(self):
        if self.last_dir:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", self.last_dir)
        else:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "./")
        self.inps_folder_dir = folder_path
        if self.inps_folder_dir:
            self.last_dir = self.inps_folder_dir
            self.lineEdit_InputFolder.setText(self.inps_folder_dir)
        return 
    
    def handleEditAbqVer(self):
        self.abaqus_ver_cmd = self.lineEdit_AbqVer.Text()
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
            self.del_expect_fileTypeList.add('sta')
        else:
            self.del_expect_fileTypeList.remove('sta')
        return 
    
    def handleToggleFileType_LOG(self, isLOGexpect):
        if isLOGexpect:
            self.del_expect_fileTypeList.add('log')
        else:
            self.del_expect_fileTypeList.remove('log')
        return 
    
    def handleToggleFileType_MSG(self, isMSGexpect):
        if isMSGexpect:
            self.del_expect_fileTypeList.add('msg')
        else:
            self.del_expect_fileTypeList.remove('msg')
        return 
    
    def handleToggleFileType_DAT(self, isDATexpect):
        if isDATexpect:
            self.del_expect_fileTypeList.add('dat')
        else:
            self.del_expect_fileTypeList.remove('dat')
        return 
    
    def handleToggleFileType_RES(self, isRESexpect):
        if isRESexpect:
            self.del_expect_fileTypeList.add('res')
        else:
            self.del_expect_fileTypeList.remove('res')
        return 
    
    def handleToggleFileType_STT(self, isSTTexpect):
        if isSTTexpect:
            self.del_expect_fileTypeList.add('stt')
        else:
            self.del_expect_fileTypeList.remove('stt')
        return 
    
    def handleSubmit(self):
        self.inps_list = self.get_inp_list(self.inps_folder_dir)
        self.submit_inps(self.inps_list, self.abaqus_ver_cmd, self.cpus_num)
        if self.isDeleteFiles:
            exclude_ls = {'inp', 'odb'} | self.del_expect_fileTypeList
            self.deletefiles(self.inps_folder_dir , self.inps_list, exclude_ls)
        return
    
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
    
    def submit_inps(self, inp_file_list, abqcmd='abaqus', cpu_num=8):
        total_jobs_num = len(inp_file_list)
        for idx, job in enumerate(inp_file_list):
            cmd_string = "{0} job={1} cpus={2} int ask=off".format(abqcmd, job, cpu_num)
            self.setWindowTitle('AbqJobSubmitter-Current/Total: {0}/{1}'.format(idx+1, total_jobs_num))
            run_cmd_Popen_fileno(cmd_string, file_path=self.inps_folder_dir)
            
    def deletefiles(self, file_path, inp_file_list, exclude_file_type={'inp', 'odb'}):
        file_ls = os.listdir(file_path)
        for file in file_ls:
            f_path = os.path.join(file_path, file)
            if os.path.isdir(f_path):
                continue
            elif not file.split(".")[0] in inp_file_list:
                continue
            elif file.split(".")[-1] in exclude_file_type:
                continue
            else:
                os.remove(f_path)
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = SubmitterWindow()
    ex.show()
    sys.exit(app.exec_())