#------------------------------------------------------------------------------
# HubFactory(RegistrationFactory) configuration
#------------------------------------------------------------------------------

## The Configurable for setting up a Hub.

# accept connections from any ip
## IP on which to listen for client connections. [default: loopback]
c.HubFactory.client_ip = '*'

# accept connections from any ip
## IP on which to listen for engine connections. [default: loopback]
c.HubFactory.engine_ip = '*'
