import bpy

""" USER SETUP
Operations applies only on active jobs
"""

modify_resolution = False
resolution = '512' # from 64 to 8192, power of two

modify_samples = False
samples = 256 # number

modify_device = False
device = 'GPU' # CPU or GPU

modify_colorspace = False
colorspace = 'Linear' # Linear, sRGB or Non-Color

# Atlas Mode specific

modify_distance = False
distance = 0.5 # number

modify_bias = False
bias = 0.25 # number

""" USER SETUP END
"""

scene = bpy.context.scene

def list_jobs_id_and_name():
    for index in range(len(scene.BakeTool_Jobs.Jobs)):
        print("{} - {}".format(index, scene.BakeTool_Jobs.Jobs[index].name))
        
def set_resolution_on_enabled_jobs(size):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled:
            for Pass in job.job_pass.Pass:
                Pass.size = size

def set_samples_on_enabled_jobs(sample):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled:
            for Pass in job.job_pass.Pass:
                Pass.samples = sample

def set_devices_on_enabled_jobs(device):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled:
            job.job_settings.render_device = device

def set_colorspace_on_enabled_jobs(space):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled:
            for Pass in job.job_pass.Pass:
                Pass.colors_space = space

def set_distance_on_enabled_jobs(distance):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled and job.job_settings.mode == 'ATLAS':
            job.job_settings.distance = distance

def set_bias_on_enabled_jobs(bias):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled and job.job_settings.mode == 'ATLAS':
            job.job_settings.bias = bias

list_jobs_id_and_name()
if modify_resolution:
    set_resolution_on_enabled_jobs(resolution)
if modify_samples:
    set_samples_on_enabled_jobs(samples)
if modify_device:
    set_devices_on_enabled_jobs(device)
if modify_colorspace:
    set_colorspace_on_enabled_jobs(colorspace)
if modify_distance:
    set_distance_on_enabled_jobs(distance)
if modify_bias:
    set_bias_on_enabled_jobs(bias)