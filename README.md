## [SportsGames BACKEND](https://github.com/Jyustin/tri3NATMdevsBackend)
Runtime link: https://tri3dev.duckdns.org/

### GETTING STARTED

- Cloning the Backend Repository for Transferability

```bash
mkdir ~/vscode; cd ~/vscode

git clone [https://github.com/Jyustin/tri3NATMdevsBackend.git]
cd tri3NATMdevsBackend
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
