# the security-setup script

The `security-setup` script is located in the root of the project. It
will set up authentication and authorization for you, as described in
the component
documentation \<../components/index\>. When components are updated, you
can run it again, as many times as you want. It will only set the
variables it needs to.

After you've set up security with the script, you can include it in your
playbook runs by specifying the `-e` or `--extra-vars` option, like so:

    ansible-playbook --extra-vars=@security.yml your_playbook.yml

## Certificates

If not present, `security-setup` will create a root CA to generate
certificates from. If you want to use your own CA, add the key in
`ssl/private/cakey.pem` and the cert in `ssl/cacert.pem`.

If you have your own (self)signed certificates, you can put them in
`ssl/private/your.key.pem` and `ssl/certs/your.cert.pem`. Just override
the locations the script generates (for example the consul key and cert
would be `ssl/private/consul.key.pem` and `ssl/certs/consul.cert.pem`,
respectively) and they'll be used instead of the generated files, and
not overridden.

In the event that you need to regenerate a certificate, rename or delete
the appropriate CSR and certificate from the `certs` folder and the
private component in `private` and re-run `security-setup`.

## Boolean Options

Options like `--mesos` take a boolean argument. You can use the
following values in these options:

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Interpreted as</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>t</td>
<td>True</td>
</tr>
<tr class="even">
<td>T</td>
<td>True</td>
</tr>
<tr class="odd">
<td>1</td>
<td>True</td>
</tr>
<tr class="even">
<td>True</td>
<td>True</td>
</tr>
<tr class="odd">
<td>true</td>
<td>True</td>
</tr>
<tr class="even">
<td>f</td>
<td>False</td>
</tr>
<tr class="odd">
<td>F</td>
<td>False</td>
</tr>
<tr class="even">
<td>0</td>
<td>False</td>
</tr>
<tr class="odd">
<td>False</td>
<td>False</td>
</tr>
<tr class="even">
<td>false</td>
<td>False</td>
</tr>
</tbody>
</table>

## Options

