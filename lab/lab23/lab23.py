import matplotlib.pyplot as plt

def plot_histogram():
    gpa_data, sat_data = read_csv_data()
    plt.hist(gpa_data)
    plt.savefig('gpa.png')
    #plt.show()
    plt.clf()
    
    plt.hist(sat_data)
    plt.savefig('sat_score.png')
    #plt.show()
    plt.clf()
    


def plot_scatter():
    gpa_data, sat_data = read_csv_data()
    plt.scatter(gpa_data, sat_data)
    plt.savefig('correlation.png')
    #plt.show()
    plt.clf()


def plot_spectra():
    spec_data_1 = read_spec_data('spectrum1.txt')
    wave_data_1 = []
    flux_data_1 = []
    for line in spec_data_1:
        wave_data_1.append(line[0])
        flux_data_1.append(line[1])
    spec_data_2 = read_spec_data('spectrum2.txt')
    wave_data_2 = []
    flux_data_2 = []
    for line in spec_data_2:
        wave_data_2.append(line[0])
        flux_data_2.append(line[1])
    
    
    plt.plot(wave_data_1, flux_data_1, 'b')
    plt.plot(wave_data_1, flux_data_2, 'g')
    plt.savefig('spectra.png')
    #plt.show()
    plt.clf()

def read_csv_data():
    csv_file = open('admission_algorithms_dataset.csv', 'r')
    
    csv_data = []
    csv_file.readline()
    for line in csv_file:
        line_data = line.split(',')
        better_data = []
        for item in line_data:
            try:
                item = float(item)
                better_data.append(item)
            except Exception:
                better_data.append(item)
        csv_data.append(better_data)
    csv_file.close()
    
    sat_data = []
    gpa_data = []
    for line in csv_data:
        sat_data.append(line[1])
        gpa_data.append(line[2])
    
    return gpa_data, sat_data

def read_spec_data(filename):
    spec_file = open(filename, 'r')
    
    spec_data = []
    for line in spec_file:
        line_data = line.split()
        better_data = []
        for item in line_data:
            item = float(item)
            better_data.append(item)
        spec_data.append(better_data)
    spec_file.close()
    
    return spec_data

def main():
    
    plot_histogram()
    plot_scatter()
    plot_spectra()


if __name__ == "__main__":
    main()
