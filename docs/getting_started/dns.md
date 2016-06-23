# DNS

> **note**
> 
> new in version 0.3

Terraform lets you configure DNS for your instances. The DNS provider is
loosely coupled from the server provider, so you could for example use
the dnsimple provider for either OpenStack or AWS hosts, or use the
Google Cloud DNS provider for DigitalOcean hosts.

## Providers

These are the supported DNS providers:

\[TOC\] ontrol\_subdomain The name for the control group (to generate
`control.yourdomain.com`.) By default, this is `control`, but you can
change it to whatever you'd like.

