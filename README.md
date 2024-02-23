# pass2proton

Export [passwordstore](https://www.passwordstore.org/) passwords to a format that [Proton Pass](https://proton.me/pass) can import.


## About

Parses your local [passwordstore](https://www.passwordstore.org/) and outputs in a CSV format that can be imported into [Proton Pass](https://proton.me/pass).  

Notes will be parsed and key/value pairs separated with a `:` will be parsed.
- The fields `username`, `user` and `email` will be parsed as the username
- The fields `url` and `href` will be parsed as the URL

All notes will be retained as notes in the CSV.


## Usage

```shell
./pass2proton.py ~/.password-store > to-import.csv
```
