# Using the Dockerfile

> **note**
> 
> new in version 0.3.1

> **note**
> 
>   - Please review the getting started guide \<./index\> for more  
>     detailed information about setting up a cluster.

## Setup

1.  Before you begin, it is recommended that you run the security-setup
    script \<../security/security\_setup\> to configure authentication
    and authorization for the various components.

<!-- end list -->

  - 2\. Next, you will need to setup a Terraform template (`*.tf` file)
    in the root  
    directory for the cloud provider of your choices. See the following
    links for more information:
    
    \[TOC\]

erraform template, and custom playbook that you configured in the Setup
above.

> **note**
> 
>   - If you have customized your Terraform template to use a different
>     SSH  
>     public key than the default `~/.ssh/id_rsa.pub`, you can specify
>     the corresponding private key as an environment variable
>     (`SSH_KEY`) when running the container. For example:
> 
> `docker run -it -e SSH_KEY=/root/.ssh/otherpvtkey -v ~/.ssh/:/ssh/ -v
> $PWD:/state mi`

