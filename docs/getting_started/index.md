# Getting Started

> **note**
> 
>   - This document assumes you have a working Ansible
>     >     >     >     >     >     >     >     installation\_. If you don't, install Ansible before  
>     continuing. This can be done simply by running `pip install -r
>     requirements.txt` from the root of the project.
> 
> It also assumes you have a working Terraform installation. You can
> download Terraform from Terraform downloads\_.

# General Information about Mantl with Ansible

The Mantl project uses Ansible to bring up nodes and clusters. This
generally means that you need three things:

1.  Hosts to use as the base for your cluster
2.  An inventory file\_ with the hosts you want to be modified. Mantl
    includes an Ansible inventory for terraformed hosts, terraform.py\_.
3.  A playbook matching Ansible roles to hosts. Mantl organizes its
    components in sample.yml\_, which we recommend copying to
    `mantl.yml` for the possibility of later customization. You can read
    more about playbooks\_ in the Ansible docs\_.

## Preparing to provision Cloud Hosts

The playbooks and roles in this project will work on whatever provider
(or metal) you care to spin up, as long as it can run CentOS 7 or
equivalent.

Your hosts will have to be accessible with your SSH key. If you're
unfamiliar with SSH keys, please read [DigitalOcean's guide to setting
up SSH
keys](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2).

Here are some guides specific to each of the platforms that Mantl
supports:

\[TOC\] ou can also provision your cluster by running a docker
container. See dockerfile for more information.

