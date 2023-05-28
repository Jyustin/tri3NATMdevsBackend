## [SportsGames BACKEND](https://github.com/nighthawkcoders/flask_portfolio)
Runtime link: https://tri3dev.duckdns.org/

### Quick way to get started
> Quick steps with MacOS or WSL; this uses Nix for programmatic way to build tools and dependencies.


- Open a Terminal, install nix which requires admin password: 
```bash
sh <(curl -L https://nixos.org/nix/install)
```

- ***Restart Terminal***

- Install Python Package helper

```bash
nix-env -if https://github.com/DavHau/mach-nix/tarball/3.5.0 -A mach-nix
```


- Open a Terminal, cd to project area

```bash
mkdir ~/vscode; cd ~/vscode

git clone [https://github.com/Jyustin/tri3NATMdevsBackend.git]
cd tri3NATMdevsBackend
```

- Build nix packages from requirements.txt

```bash
mach-nix env ./env -r requirements.txt
```

- End of nix shell setup, exit shell
```
exit
```

### Run Server or run VSCode

- Run nix shell (virtual environment)

```bash
nix-shell ./env
```

- Run from Terminal without VSCode

    - Run python from command line and check server
    ```bash
    python main.py
    ```

- Prepare VSCode and run
    
    - From Terminal run VSCode
    ```bash
    code .
    ```

    - In VSCode open Terminal, verify Nix python
    ```bash
    which python
    ```
    - Open Setting: Ctl-Shift P or Cmd-Shift
        - Search Python: Select Interpreter
        - Match interpreter to `which output` above

    - Try Play button and try to Debug
    

### SportsGames: Why Backend?
> 
