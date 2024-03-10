# Expose Web-Server securely

- [Expose Web-Server securely](#expose-web-server-securely)
  - [localto](#localto)
  - [zrok](#zrok)
  - [Bore](#bore)
  - [localhost.run](#localhostrun)
  - [Tunnelmole](#tunnelmole)
  - [Tabserve](#tabserve)
  - [Pinggy](#pinggy)
  - [Localxpose](#localxpose)
  - [frp](#frp)
  - [sshuttle](#sshuttle)
  - [chisel](#chisel)
  - [Cloudflare tunnel](#cloudflare-tunnel)
  - [Tunnel in](#tunnel-in)
  - [ngrok](#ngrok)


## [localto](https://github.com/localtunnel/localtunnel)

* [techmonger](https://techmonger.github.io/14/localtunnel-example/)

```bash
# Installation
sudo npm install -g localtunnel

# Running
lt --port 9010 -s dartie
```

```
your url is: https://dartie.loca.lt
```

You'll be asked for a tunnel password. It can be retrieved using

```bash
# Copy password in the clipboard (requires xclip)
echo $(curl https://loca.lt/mytunnelpassword) | xclip -selection clipboard
```

as explained in the following steps

```
Are you the developer?
If you're the developer of this website, please read this:

We display this page to prevent abuse.
You and other visitors will only see this page from a standard web browser once per public IP every 7 days.
The tunnel password is the public IP of the computer running the localtunnel client (or your vpn's public IP if you're connected to one).
You'll need to share your tunnel password with your link visitors in order for them to access your content.
To get your tunnel password, you can either:

If running the localtunnel client on a local computer, visit this link in a web browser on that PC or any other PC on the same network: https://loca.lt/mytunnelpassword

If running the localtunnel client on a remote computer, ssh into the remote computer and run one of the following:
curl https://loca.lt/mytunnelpassword or wget -q -O - https://loca.lt/mytunnelpassword
To bypass this page:
Set a bypass-tunnel-reminder request header with any value
Or, set and send a custom / non-standard browser User-Agent request header
Note: it's not possible to fully remove this page for all visitors at this time.
```

## [zrok](https://zrok.io/)

* [zrok - github](https://github.com/openziti/zrok)

## [Bore](https://github.com/ekzhang/bore)

```bash
cargo install bore-cli

# ~/.cargo/bin/bore local <service-port> --to bore.pub -p <external-port>
~/.cargo/bin/bore local 9010 --to bore.pub -p 27051

```

## [localhost.run](https://localhost.run/docs/)

```bash
ssh -R 80:localhost:9010 localhost.run

```

## [Tunnelmole](https://github.com/robbie-cahill/tunnelmole-client)

* [Tunnelmole-service](https://github.com/robbie-cahill/tunnelmole-service)

## [Tabserve](https://tabserve.dev/)

## [Pinggy](https://pinggy.io/)

## [Localxpose](https://localxpose.io/)

## [frp](https://github.com/fatedier/frp)

## [sshuttle](https://github.com/sshuttle/sshuttle)

## [chisel](https://github.com/jpillora/chisel)


## [Cloudflare tunnel](https://dash.cloudflare.com/)

* [Programmingpercy](https://programmingpercy.tech/blog/free-secure-self-hosting-using-cloudflare-tunnels/)


## [Tunnel in](https://tunnelin.com/)

## [ngrok](https://ngrok.com/)

* [dev.to](https://dev.to/antopiras89/expose-your-work-with-ngrok-and-localtunnel-1p0j)
