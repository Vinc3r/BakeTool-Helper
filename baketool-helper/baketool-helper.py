import bpy

"""CHOIX UTILISATEUR
les opérations ne s'appliquent que sur les jobs activés
"""

changer_resolution = False
resolution = '512' # renseigner une valeur présente dans le menu déroulant de baketool, conserver le charactere '

changer_samples = False
samples = 256 # renseigner un chiffre

changer_device = False
device = 'GPU' # CPU ou GPU, conserver le charactere '

change_colorspace = False
colorspace = 'linear' # linear, sRGB


"""DO NOT TOUCH
"""

scene = bpy.context.scene

def list_jobs_id_and_name():
    for index in range(len(scene.BakeTool_Jobs.Jobs)):
        print("{} - {}".format(index, scene.BakeTool_Jobs.Jobs[index].name))
        
def set_resolution_on_enabled_jobs(size):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled:
            job.job_pass.Pass[0].size = size

def set_samples_on_enabled_jobs(sample):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled:
            job.job_pass.Pass[0].samples = sample

def set_devices_on_enabled_jobs(device):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled:
            job.job_settings.render_device = device

def set_colorspace_on_enabled_jobs(space):
    for job in scene.BakeTool_Jobs.Jobs:
        if job.enabled:
            job.job_pass.Pass[0].colors_space = space

list_jobs_id_and_name()
if changer_resolution:
    set_resolution_on_enabled_jobs(resolution)
if changer_samples:
    set_samples_on_enabled_jobs(samples)
if changer_device:
    set_devices_on_enabled_jobs(device)
if change_colorspace:
    set_colorspace_on_enabled_jobs(colorspace)