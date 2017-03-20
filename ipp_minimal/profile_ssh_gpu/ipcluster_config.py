# Configuration file for ipcluster.

c = get_config()

# increase timeouts, just in case
c.IPEngineApp.wait_for_url_file = 60
c.EngineFactory.timeout = 60

# set the engine launcher class to ssh
# this can be abbreviated to 'SSH'
c.IPClusterEngines.engine_launcher_class = 'SSHEngineSetLauncher'

#------------------------------------------------------------------------------
# SSHLauncher(LocalProcessLauncher) configuration
#------------------------------------------------------------------------------

## A minimal launcher for ssh.
#
#  To be useful this will probably have to be extended to use the ``sshx`` idea
#  for environment variables.  There could be other things this needs as well.

## hostname on which to launch the program
#c.SSHLauncher.hostname = ''

## user@hostname location for ssh in one setting
#c.SSHLauncher.location = ''

## args to pass to scp
#c.SSHLauncher.scp_args = []

## command for sending files
#c.SSHLauncher.scp_cmd = ['scp']

## args to pass to ssh
#c.SSHLauncher.ssh_args = ['-tt']

## command for starting ssh
#c.SSHLauncher.ssh_cmd = ['ssh']


# NOTE: don't send any files because we're on NFS
## List of (remote, local) files to fetch after starting
c.SSHLauncher.to_fetch = []

## List of (local, remote) files to send before starting
c.SSHLauncher.to_send = []

## username for ssh
c.SSHLauncher.user = 'bergera'

#------------------------------------------------------------------------------
# SSHEngineSetLauncher(LocalEngineSetLauncher) configuration
#------------------------------------------------------------------------------

## dict of engines to launch.  This is a dict by hostname of ints, corresponding
#  to the number of engines to start on that host.
c.SSHEngineSetLauncher.engines = {
   'turagas-ws2': 1,
    'turagas-ws4': 1
}

# NOTE: this is crucial, engine's must know where to look for the controller
c.SSHEngineSetLauncher.engine_args = ['--location="turagas-ws4"']
c.SSHEngineSetLauncher.engine_cmd = ['/groups/turaga/home/bergera/anaconda3/envs/tf_gpu/bin/python', '-m', 'ipyparallel.engine']
