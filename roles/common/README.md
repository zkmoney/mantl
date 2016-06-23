# Common

> **note**
> 
> new in version 0.1

The common role prepares a system with functionality needed between
multiple roles. Specifically:

  - sets timezone to UTC
  - configures hosts for simple name resolution (before Consul DNS is
    set up)
  - installs common software like pip
  - adds users \</getting\_started/ssh\_users\>.
  - adds SSL certificates created by security-setup
    \</security/security\_setup\> to the root CA store
  - does various workarounds for cloud providers

## Variables

  - use\_host\_domain  
    Add a domain component to hosts in /etc/hosts
    
    default: `false`

  - host\_domain  
    The domain component to add to hosts in /etc/hosts
    
    default: `novalocal`

