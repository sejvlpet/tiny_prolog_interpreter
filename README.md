# Tiny Prolog interpreter

Napište program, který bude umět vyhodnocovat podmnožinu Prologu

Minimální požadavky
- Vaše aplikace musí:

    - vyhodnotit alespoň programy na úrovni výpočtu faktoriálu (tedy clauses, predicates, aritmetiku a prohledávání stavového prostoru).
- Extra body
    - Extra body jsou za následující rozšíření: implementace řezů

## Example usage
- run tiny_prolog_interpreter using Python 3
- load Database usign command:
  - consult(<file_path>).
- start entering questions:
  - question starts with ?- and ends with .
  - question can be given to clauses (like ?-fact(5, 120).), or to check a computation (like ?- 10 is 5 + 5.)

### Real example of commands

Use those commands and see the results to check the mandatory features:

- consult(tests/test_files/sumup_fact_fib).
- ?- fact(5, X).
- ?- fib(10, X).
- ?- sumup(4, X).
- ?- fact(4, 24).

Use those commands to check the extra features - cuts:

- consult(tests/test_files/load4).
- ?- fact(5, X).
- consult(tests/test_files/load5).
- ?- fact(5, X).

This should show the difference between cutting and not. I'm aware that behavior of factorial loaded from tests/test_files/load4
is not the same as the behavior as it would be in Prolog (which stops when it reaches a fact, yet my TinyProlog moves on to the rules),
but it seemed OK to me to let it this way for simpler testing.

### Tests
To see more test, please check tests/main_test.py file.

You can run them from repository root using:
- python -m tests.main_test


### Rule and facts syntax
Please check the tests/test_files/sumup_fact_fib to see example of syntax for rules and facts. Syntax is based on Prolog,
but is slightly simplified. Also, please note that for simplicity, negative numbers are not supported and a variable name
cannot be contained in another variable name (Res and SubRes for example), those would cause an undefined behavior.