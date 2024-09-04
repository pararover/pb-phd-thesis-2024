num_peaks = 100   # Set this to a high enough value so that sufficient red dots
                  # mark the peaks of interest, compared with above plot
peak_indices = np.argpartition(power01, -num_peaks)[-num_peaks:]

plt.plot(peak_indices, power01[peak_indices], 'ro')
for i in range(len(peak_indices)):
    plt.text(peak_indices[i], power01[peak_indices[i]], str(peak_indices[i]))

plt.title('Note down index values of peaks');