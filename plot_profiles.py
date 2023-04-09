# import pylab
import modeller
from matplotlib import pyplot as plt
# import bokeh
# from bokeh.plotting import figure, output_file, save

def r_enumerate(seq):
    """Enumerate a sequence in reverse order"""
    # Note that we don't use reversed() since Python 2.3 doesn't have it
    num = len(seq) - 1
    while num >= 0:
        yield num, seq[num]
        num -= 1

def get_profile(profile_file, seq):
    """Read `profile_file` into a Python array, and add gaps corresponding to
       the alignment sequence `seq`."""
    # Read all non-comment and non-blank lines from the file:
    f = open(profile_file)
    vals = []
    for line in f:
        if not line.startswith('#') and len(line) > 10:
            spl = line.split()
            vals.append(float(spl[-1]))
    # Insert gaps into the profile corresponding to those in seq:
    for n, res in r_enumerate(seq.residues):
        for gap in range(res.get_leading_gaps()):
            vals.insert(n, None)
    # Add a gap at position '0', so that we effectively count from 1:
    vals.insert(0, None)
    return vals

e = modeller.Environ()
a = modeller.Alignment(e, file='Target-template.ali')

template = get_profile('Template.profile', a['3u4wA'])
model = get_profile('Target.profile', a['1YES'])

# Plot the template and model profiles in the same plot for comparison:
plt.figure(1, figsize=(10,6))
plt.xlabel('Alignment position')
plt.ylabel('DOPE per-residue score')
plt.plot(model, color='red', linewidth=2, label='Model')
plt.plot(template, color='green', linewidth=2, label='Template')
plt.legend()
plt.savefig('dope_profile.png', dpi=65)
#
# output_file('dope_profile.html')
# p = figure(title="DOPE per-residue score",
#            x_axis_label='Alignment position',
#            y_axis_label='DOPE per-residue score')
#
# # Add the template and model data to the plot
# p.line(range(len(model)), model, line_color='red', line_width=2, legend_label='Model')
# p.line(range(len(template)), template, line_color='green', line_width=2, legend_label='Template')
#
# # Add the legend
# p.legend.location = 'top_left'
#
# # Save the plot
# save(p)