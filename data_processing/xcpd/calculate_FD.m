clc;
clear;
close all;
% addpath('/GPFS/cuizaixu_lab_permanent/xulongzhou/apps/fieldtrip');
% ft_default;
site_dir = dir('/GPFS/cuizaixu_lab_permanent/Public_Data/ABCD/ABCC/rawdata/rsfMRI/SIEMENS/site*');
for site_num = 1:length(site_dir)
    subj_dir = dir(fullfile(site_dir(site_num).folder, site_dir(site_num).name, 'sub*'));
    n = 0;
    n010 = 0;
    n015 = 0;
    n020 = 0;
    n025 = 0;
    for subj_num = 1:length(subj_dir)
        disp(site_dir(site_num).name);
        disp(subj_dir(subj_num).name);
        % find motion files
        fd_file = dir(fullfile(subj_dir(subj_num).folder, subj_dir(subj_num).name, 'ses-*', 'func', '*run-1_desc-filteredincludingFD_motion.tsv'));
        if isempty(fd_file)
            continue;
        end
        % read the fd 
        motion_file = importdata(fullfile(fd_file.folder, fd_file.name));
        meanFD = mean(motion_file.data(:,13));
        MEAN_FD.site(site_num).sub(subj_num).site_name = site_dir(site_num).name;
        MEAN_FD.site(site_num).sub(subj_num).subj_name = subj_dir(subj_num).name;
        MEAN_FD.site(site_num).sub(subj_num).meanFD = meanFD;
        
        subj_list.site(site_num).site_name = site_dir(site_num).name;
        if meanFD < 0.10
            n010 = n010 + 1;
            subj_list.site(site_num).fd_smaller_010.sub(n010).subj_name = subj_dir(subj_num).name;
            subj_list.site(site_num).fd_smaller_010.sub(n010).meanFD = meanFD;
        end
        if meanFD < 0.15
            n015 = n015 + 1;
            subj_list.site(site_num).fd_smaller_015.sub(n015).subj_name = subj_dir(subj_num).name;
            subj_list.site(site_num).fd_smaller_015.sub(n015).meanFD = meanFD;
        end
        if meanFD < 0.20
            n020 = n020 + 1;
            subj_list.site(site_num).fd_smaller_020.sub(n020).subj_name = subj_dir(subj_num).name;
            subj_list.site(site_num).fd_smaller_020.sub(n020).meanFD = meanFD;
        end
        if meanFD < 0.25
            n025 = n025 + 1;
            subj_list.site(site_num).fd_smaller_025.sub(n025).subj_name = subj_dir(subj_num).name;
            subj_list.site(site_num).fd_smaller_025.sub(n025).meanFD = meanFD;
        end
    end
    save('meanFD.mat', 'MEAN_FD', 'subj_list');
end