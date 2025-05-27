def save_to_json(data, filepath):
    import json
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def export_to_pdf(data, filepath):
    from matplotlib.backends.backend_pdf import PdfPages
    import matplotlib.pyplot as plt

    with PdfPages(filepath) as pdf:
        plt.figure()
        plt.title('Wind Flow Simulation Results')
        plt.plot(data['x'], data['y'], label='Wind Flow')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        pdf.savefig()
        plt.close()