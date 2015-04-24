#==============================================================================
# This class can be used to quickly view and analyze data arrays
#==============================================================================
class QuickView:
    def __init__(self, fields, timestamp, data):    
        self.fields                         = fields
        self.timestamp                      = timestamp
        self.data                           = data
        
        self.textfontsize                   = 10
        self.hspace                         = 0.4
        self.wspace                         = 0.2
        self.x_labelrot                     = 20
        self.linewidth                      = 0.4
        self.markersize                     = 0.7
        self.barwith                        = 10
        self.gridstate                      = False
        self.scatter_plot_density_status    = False
        self.scatter_plot_density_num_bins  = 100
        self.hist_number_bins               = 100
        self.hist_normalize_mode            = False
        
        self.mean                           = []
        self.median                         = []
        self.std                            = []
        self.min                            = []
        self.max                            = []
        self.percentile25                   = []
        self.percentile75                   = []
        self.N                              = []
        
    #==============================================================================
    #     This method prints the fields, and caches some summary statistics
    #==============================================================================    
    def get_fields_and_calc_stats(self, max_columnWidth = 0):
        ''' Import modules '''        
        import numpy as np
        from tableprint import tableprint as tp
        
        ''' cache stats '''        
        if len(self.mean) == 0:
            for i in range(self.data.shape[1]):
                self.mean.append(np.mean(self.data[:,i]))
                self.median.append(np.median(self.data[:,i]))
                self.std.append(np.std(self.data[:,i]))
                self.min.append(np.min(self.data[:,i]))
                self.max.append(np.max(self.data[:,i]))
                self.percentile25.append(np.percentile(self.data[:,i], 25))
                self.percentile75.append(np.percentile(self.data[:,i], 75))                                                                                
                self.N.append(self.data[:,i].shape[0])
        
        ''' construct lists and print fields and stats '''
        table      = np.array([self.mean, self.median, self.std, self.min, self.max, self.percentile25, self.percentile75, self.N]).T
        table      = np.round(table, 4)
        table      = np.hstack((np.array([range(self.fields.shape[0])]).T, np.array([self.fields]).T, table))
        table      = np.vstack((np.array([['#',  'Fields' , 'Mean' , 'Median' , 'STD' , 'Min' , 'Max' , '25 Percent', '75 Percent', 'N']]), 
                                np.array([['--', '-------', '-----', '-------', '----', '----', '----', '-----------', '----------','--']]),
                                table))
        table      = table.tolist()
        print tp(table, max_columnWidth = max_columnWidth, justify = 'L')
               
    #==============================================================================
    #     This method plots the time series trends on separate subplots
    #==============================================================================
    def multi_timeseries(self, Col_indexes = [0], Number_of_Figures = 1):
        ''' Import modules'''        
        import matplotlib.pyplot as plt
        import numpy as np

        '''Set the number of rows and cols per Figure'''
        plots_per_figure     =  int(np.ceil(len(Col_indexes)/float(Number_of_Figures)))   
        num_cols_per_subplot =  1        
        num_rows_per_subplot =  1
        while (num_rows_per_subplot*num_cols_per_subplot < plots_per_figure):
            num_rows_per_subplot = num_rows_per_subplot + 1
        
        ''' Plot Data'''                   
        i = 0 
        for fig_index in range(1, Number_of_Figures + 1):
            plt.figure('multi_timeseries' + ' ' + str(fig_index), facecolor = 'white')
            plt.subplots_adjust(hspace = self.hspace)
            
            ax = plt.subplot(num_rows_per_subplot, num_cols_per_subplot, 1)
            ax.plot(self.timestamp, self.data[:,Col_indexes[i]], 'b-', linewidth = self.linewidth)
            plt.grid(self.gridstate)
            
            plt.title(self.fields[Col_indexes[i]], fontsize = self.textfontsize)
            plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1) 
            
            locs, labels = plt.xticks()
            plt.setp(labels, rotation = self.x_labelrot)
            i = i + 1
            
            if i == len(Col_indexes):
                break
            
            for subplot_int in range(1, plots_per_figure + 1): 
                if subplot_int == 1:
                    continue
                plt.subplot(num_rows_per_subplot, num_cols_per_subplot, subplot_int, sharex = ax)                         
                plt.plot(self.timestamp, self.data[:,Col_indexes[i]], 'b-', linewidth = self.linewidth)
                plt.grid(self.gridstate)
                
                plt.title(self.fields[Col_indexes[i]], fontsize = self.textfontsize)
                plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)                
                
                locs, labels = plt.xticks()
                plt.setp(labels, rotation = self.x_labelrot)                                
                i = i + 1
                
                if i == len(Col_indexes):
                    break
        
    #==============================================================================
    #     This met1hod plots the time series trends on a single subplot        
    #==============================================================================
    def single_timeseries(self, Left_ax_Col_indexes  = [0],    Right_ax_Col_indexes  = [],
                                Left_ax_label        = ' ',    Right_ax_label        = ' '):
        ''' Import modules'''        
        import matplotlib.pyplot as plt
        
        ''' Plot Data'''
        plt.figure('single_timeseries', facecolor = 'white')
        ax = plt.subplot()        
        for colIndex in Left_ax_Col_indexes:
            ax.plot(self.timestamp, self.data[:,colIndex], linewidth = self.linewidth, label = self.fields[colIndex])
        plt.grid(self.gridstate)
        plt.ylabel(Left_ax_label, fontsize = self.textfontsize)
        plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)
        plt.legend(loc = 'upper left', fontsize = self.textfontsize)
        locs, labels = plt.xticks()
        plt.setp(labels, rotation = self.x_labelrot) 
        if len(Right_ax_Col_indexes) != 0:        
            ax = ax.twinx()
            for colIndex in Right_ax_Col_indexes:
                ax.plot(self.timestamp, self.data[:,colIndex], linewidth = self.linewidth, label = self.fields[colIndex])
            plt.ylabel(Right_ax_label, fontsize = self.textfontsize)
        plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)
        plt.legend(loc = 'upper right', fontsize = self.textfontsize) 

    #==============================================================================
    #     This method plots the time series trends on separate subplots
    #==============================================================================
    def multi_bar_timeseries(self, Col_indexes = [0], Number_of_Figures = 1):
        ''' Import modules'''        
        import matplotlib.pyplot as plt
        import numpy as np

        '''Set the number of rows and cols per Figure'''
        plots_per_figure     =  int(np.ceil(len(Col_indexes)/float(Number_of_Figures)))   
        num_cols_per_subplot =  1        
        num_rows_per_subplot =  1
        while (num_rows_per_subplot*num_cols_per_subplot < plots_per_figure):
            num_rows_per_subplot = num_rows_per_subplot + 1
        
        ''' Plot Data'''                   
        i = 0 
        for fig_index in range(1, Number_of_Figures + 1):
            plt.figure('multi_bar_timeseries' + ' ' + str(fig_index), facecolor = 'white')
            plt.subplots_adjust(hspace = self.hspace)
            
            ax = plt.subplot(num_rows_per_subplot, num_cols_per_subplot, 1)
            ax.bar(self.timestamp, self.data[:,Col_indexes[i]], width = self.barwith)
            plt.grid(self.gridstate)
            
            plt.title(self.fields[Col_indexes[i]], fontsize = self.textfontsize)
            plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1) 
            
            locs, labels = plt.xticks()
            plt.setp(labels, rotation = self.x_labelrot)
            i = i + 1
            
            if i == len(Col_indexes):
                break
            
            for subplot_int in range(1, plots_per_figure + 1): 
                if subplot_int == 1:
                    continue
                plt.subplot(num_rows_per_subplot, num_cols_per_subplot, subplot_int, sharex = ax)                         
                plt.bar(self.timestamp, self.data[:,Col_indexes[i]], width = self.barwith)
                plt.grid(self.gridstate)
                
                plt.title(self.fields[Col_indexes[i]], fontsize = self.textfontsize)
                plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)                
                
                locs, labels = plt.xticks()
                plt.setp(labels, rotation = self.x_labelrot)                                
                i = i + 1
                
                if i == len(Col_indexes):
                    break
                
    #==============================================================================
    #     This method plots the bar time series trends on a single subplot        
    #==============================================================================
#    def single_bar_timeseries(self, Left_ax_Col_indexes  = [0],    Right_ax_Col_indexes  = [],
#                                    Left_ax_label        = ' ',    Right_ax_label        = ' '):
#        ''' Import modules'''        
#        import matplotlib.pyplot as plt
#        import numpy as np
#        
#        ''' Plot Data'''
#        plt.figure('single_bartimeseries', facecolor = 'white')
#        ax = plt.subplot()
#        count = 0 
#        bins  = np.array(range(len(self.timestamp)))
#        color_list = ['b','g','r','y','k']
#        for colIndex in Left_ax_Col_indexes:
#            ax.bar(bins + self.barwith*count, self.data[:,colIndex], width = self.barwith, label = self.fields[colIndex], color = color_list[count])
#            count = count + 1
#        plt.grid(self.gridstate)
#        plt.ylabel(Left_ax_label, fontsize = self.textfontsize)
#        plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)
#        plt.legend(loc = 'upper left', fontsize = self.textfontsize)
#        locs, labels = plt.xticks()
#        plt.setp(labels, rotation = self.x_labelrot) 
#        if len(Right_ax_Col_indexes) != 0:        
#            ax = ax.twinx()
#            for colIndex in Right_ax_Col_indexes:
#                ax.bar(bins + self.barwith*count, self.data[:,colIndex], width = self.barwith, label = self.fields[colIndex], color = color_list[count])
#                count = count + 1
#            plt.ylabel(Right_ax_label, fontsize = self.textfontsize) 
#        plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)
#        plt.legend(loc = 'upper right', fontsize = self.textfontsize) 

    #==============================================================================
    #      This method constructs scatter plots on different subplots
    #==============================================================================
    def multi_scatter(self,   y_axis_Col_index  = 0,   x_axis_Col_indexes = [0],  
                              Number_of_Figures = 1):
        ''' Import modules'''        
        import matplotlib.pyplot as plt
        import numpy as np
        
        '''Set the number of rows and cols per Figure'''
        plots_per_figure     =  int(np.ceil(len(x_axis_Col_indexes)/float(Number_of_Figures)))
        num_cols_per_subplot =  int(plots_per_figure**0.5)        
        num_rows_per_subplot =  int(plots_per_figure**0.5)
        
        while (num_rows_per_subplot*num_cols_per_subplot < plots_per_figure):
            num_rows_per_subplot = num_rows_per_subplot + 1 

        ''' Plot Data'''                   
        i = 0 
        for fig_index in range(1, Number_of_Figures + 1):
            plt.figure('multi_scatter' + ' ' + str(fig_index), facecolor = 'white').suptitle('Scatter plot with respect to ' + self.fields[y_axis_Col_index], fontsize = self.textfontsize + 2)
            plt.subplots_adjust(hspace = self.hspace, wspace = self.wspace)
            for subplot_int in range(1, plots_per_figure + 1): 
                plt.subplot(num_rows_per_subplot, num_cols_per_subplot, subplot_int)
                correlation =  np.corrcoef(self.data[:, x_axis_Col_indexes[i]], self.data[:, y_axis_Col_index])[0,1]                 
                if self.scatter_plot_density_status:
                    plt.hist2d(self.data[:, x_axis_Col_indexes[i]], self.data[:, y_axis_Col_index], bins = self.scatter_plot_density_num_bins)                
                    plt.annotate('Correlation:  ' + str(np.round(correlation,3)), xy=(0.1, 0.9), xycoords='axes fraction', fontsize = self.textfontsize, color = 'white')                                
                else:
                    plt.plot(self.data[:, x_axis_Col_indexes[i]], self.data[:, y_axis_Col_index], '.', markersize = self.markersize)
                    plt.annotate('Correlation:  ' + str(np.round(correlation,3)), xy=(0.1, 0.9), xycoords='axes fraction', fontsize = self.textfontsize)
                plt.xlabel(self.fields[x_axis_Col_indexes[i]], fontsize = self.textfontsize)
                plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)
                i = i + 1
                plt.grid(self.gridstate)
                if i == len(x_axis_Col_indexes):
                    break                                     
                
            
    #==============================================================================
    #      This method constructs a single scatter plot
    #==============================================================================                                     
    def single_scatter(self, y_axis_Col_index = 0, x_axis_Col_indexes = [0]):
        ''' Import modules'''        
        import matplotlib.pyplot as plt
        import numpy as np 
        
        ''' Plot Data'''
        plt.figure('single_scatter', facecolor = 'white')
        for colIndex in x_axis_Col_indexes:
            correlation =  np.corrcoef(self.data[:, colIndex], self.data[:, y_axis_Col_index])[0,1]
            label_text  =  self.fields[colIndex] + '   |   Correlation:  ' + str(np.round(correlation,3))
            if self.scatter_plot_density_status:
                plt.hist2d(self.data[:, colIndex], self.data[:, y_axis_Col_index], bins = self.scatter_plot_density_num_bins, label = label_text)
            else:
                plt.plot(self.data[:, colIndex], self.data[:, y_axis_Col_index], '.', markersize = self.markersize, label = label_text)
         
        plt.ylabel(self.fields[y_axis_Col_index], fontsize = self.textfontsize)
        plt.legend(loc = 'upper left', fontsize = self.textfontsize)
        plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)                
        plt.grid(self.gridstate) 
        
    #==============================================================================
    #      This method constructs histograms on different subplots
    #==============================================================================
    def multi_hist(self, Col_indexes = [0], Number_of_Figures = 1):           
        ''' Import modules'''        
        import matplotlib.pyplot as plt
        import numpy as np
        
        '''Set the number of rows and cols per Figure'''
        plots_per_figure     =  int(np.ceil(len(Col_indexes)/float(Number_of_Figures)))
        num_cols_per_subplot =  int(plots_per_figure**0.5)        
        num_rows_per_subplot =  int(plots_per_figure**0.5)
        
        while (num_rows_per_subplot*num_cols_per_subplot < plots_per_figure):
            num_rows_per_subplot = num_rows_per_subplot + 1 
                                     
        ''' Plot Data'''                   
        i = 0 
        for fig_index in range(1, Number_of_Figures + 1):
            plt.figure('multi_hist' + ' ' + str(fig_index), facecolor = 'white')
            plt.subplots_adjust(hspace = self.hspace, wspace = self.wspace)

            for subplot_int in range(1, plots_per_figure + 1): 
                plt.subplot(num_rows_per_subplot, num_cols_per_subplot, subplot_int)
                plt.hist(self.data[:, Col_indexes[i]], self.hist_number_bins, normed = self.hist_normalize_mode)
                
                if len(self.mean) == 0:
                    text = ' '
                else:
                    text = ('\nMean:    '   + str(np.round(self.mean[Col_indexes[i]],2))  +
                            '\nMedian: '   + str(np.round(self.median[Col_indexes[i]],2)) +
                            '\nSTD:      '   + str(np.round(self.std[Col_indexes[i]],2))  +
                            '\nN:          '   + str(self.N[Col_indexes[i]]))
                            
                plt.annotate(text, xy=(0.1, 0.6), xycoords='axes fraction', fontsize = self.textfontsize - 1)
                plt.xlabel(self.fields[Col_indexes[i]], fontsize = self.textfontsize)
                plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)
                i = i + 1
                plt.grid(self.gridstate)
                if i == len(Col_indexes):
                    break
             
                                                                         
    #==============================================================================
    #      This method constructs a single histogram
    #==============================================================================                                     
    def single_hist(self, Col_indexes = [0], x_axis_label = ' '):
        ''' Import modules'''        
        import matplotlib.pyplot as plt
        import numpy as np
        
        ''' Plot Data''' 
        Trans_Level = 1
        Trans_Level_reduction_rate = (1.0 - 0.3)/float((len(Col_indexes)))    
        plt.figure('single_hist', facecolor = 'white')
        plt.subplot(1,1,1)
        text = ''
        for colIndex in Col_indexes:
            plt.hist(self.data[:, colIndex], self.hist_number_bins, 
                     normed = self.hist_normalize_mode, label = self.fields[colIndex], alpha = Trans_Level)
            Trans_Level = Trans_Level - Trans_Level_reduction_rate
            if len(self.mean) == 0:
                text = ' '
            else:
                text        = (text + self.fields[colIndex] + '\n------------------'  +
                              '\nMean:    '   + str(np.round(self.mean[colIndex],2))  +
                              '\nMedian: '   + str(np.round(self.median[colIndex],2)) +
                              '\nSTD:      '   + str(np.round(self.std[colIndex],2))  +
                              '\nN:          '   + str(self.N[colIndex])              +
                              '\n\n')    
        plt.xlabel(x_axis_label, fontsize = self.textfontsize)
        plt.legend(loc = 'upper left', fontsize = self.textfontsize)
        plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)
        plt.annotate(text, xy=(0.7, 0.4), xycoords='axes fraction', fontsize = self.textfontsize - 1)
        plt.grid(self.gridstate) 
        
    #==============================================================================
    #      This method constructs multiple boxplots
    #==============================================================================
    def single_box(self, Col_indexes = [0]):
        ''' Import modules '''        
        import matplotlib.pyplot as plt
        import numpy as np
        
        plt.figure('single_box', facecolor = 'white')
        plt.boxplot(self.data[:,Col_indexes])
        
        text = ' '
        plt.tick_params(axis='both', which='major', labelsize = self.textfontsize - 1)
        for i,colIndex in enumerate(Col_indexes):
            if len(self.mean) == 0:
                text = ' '
            else:
                text        = ('\nMean:    '   + str(np.round(self.mean[colIndex],2))  +
                               '\nMedian: '   + str(np.round(self.median[colIndex],2)) +
                               '\nSTD:      '   + str(np.round(self.std[colIndex],2))  +
                               '\nN:          '   + str(self.N[colIndex])              )
            plt.text(i + 0.6, np.max(self.data[:,Col_indexes]) - np.max(self.data[:,Col_indexes])/2, 
                     text,    fontsize = self.textfontsize - 1)

        plt.xticks(range(1,len(Col_indexes) + 1), self.fields[Col_indexes], rotation = self.x_labelrot, fontsize = self.textfontsize)
        plt.grid(self.gridstate)                              