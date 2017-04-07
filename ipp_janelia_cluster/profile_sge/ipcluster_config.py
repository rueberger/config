""" Cluster config for the Janelia cluster

This profile must be named profile_sge

engine_batch_template must be adapted for your purposes
In particular, set the path to the engine on the last line
"""

import os

c = get_config()

# tells ipyparallel to use star grid engine
c.IPClusterStart.controller_launcher_class = "SGE"
c.IPClusterEngines.engine_launcher_class = "SGE"

# the number of engines in this cluster
# set the number of cores per engine in ../engine_batch_template, line 5
# the default is to use 32 cores
c.IPClusterEngines.n = 150

# path to the batch template file
c.SGEEngineSetLauncher.batch_template_file = os.path.expanduser('~/.ipython/profile_sge/engine_batch_template')


c.HubFactory.ip = '*'
c.HubFactory.engine_ip = '*'
c.HubFactory.db_class = "SQLiteDB"

c.IPEngineApp.wait_for_url_file = 60
c.EngineFactory.timeout = 60
