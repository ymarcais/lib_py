import matplotlib.pyplot as plt

class My_plots:
 #plot colors
    def plot_format(self):
        plt.gca().spines['bottom'].set_color('blue')
        plt.gca().spines['top'].set_color('blue')
        plt.gca().spines['right'].set_color('blue')
        plt.gca().spines['left'].set_color('blue')
        plt.tick_params(axis='both', colors='blue')


    # plot legend parameters
    def plot_legend(self, len_dimensions, f1_accuracy):
        label_lines =   [
            f"{len_dimensions} layers \n"
            f"F1_score: {f1_accuracy['macro_f1_score']:.2f}% \n"
            f"Recall: {f1_accuracy['macro_recall']:.2f}% \n"
            f"Precision: {f1_accuracy['macro_precision']:.2f}% \n"
            f"Test_accuracy: {f1_accuracy['test_accuracy']:.2f}% \n"
                       ]
        legend = plt.legend(label_lines,loc='center left', bbox_to_anchor=(1.0, 0.5), borderpad=1)
        legend.get_frame().set_linewidth(0)
        legend.get_frame().set_facecolor('lightblue')
        legend.get_frame().set_alpha(0.3)
        for text in legend.get_texts():
            text.set_fontsize(10)
            text.set_color('blue')

    
    #plot double charts
    def plot_presentation(self, training_history, f1_accuracy, len_dimensions):
        final_row = training_history[-1]
        final_value = final_row[-1]
        title_lines =   [
		f"Training set accuracy: {final_value:.2f}%"
                        ]
        title = '\n'.join(title_lines)

        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.subplots_adjust(left=0.05)
        plt.plot(training_history[:, 0], label='train loss', color='red', linewidth=3)
        plt.title(f"Training set cost loss:", color='blue')
        self.plot_format()

        plt.subplot(1, 2, 2)
        plt.subplots_adjust(right=0.80)
        plt.plot(training_history[:, 1], label='train acc', color='red', linewidth=3)
        plt.title(title, color='blue')
        self.plot_format()
        self.plot_legend(len_dimensions, f1_accuracy)        

        plt.show()