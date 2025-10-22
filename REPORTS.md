# Automated Reports
## Coverage Report
```text
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
CLI.py                       117     68    42%   59, 72-77, 100-101, 111-169, 186-209, 212-213
Tests/__init__.py              0      0   100%
Tests/test_backgammon.py      87      0   100%
Tests/test_dice.py            48      1    98%   89
Tests/test_player.py          24      1    96%   45
Tests/tests_board.py          52      1    98%   76
Tests/tests_checker.py        35      1    97%   59
Tests/tests_cli.py           102     19    81%   50-51, 59-60, 68-69, 110-111, 119-120, 129-130, 139-140, 152-153, 161-162, 166
core/BackgammonGame.py        82     26    68%   77-82, 99, 107-111, 121-124, 128-134, 150, 185-188
core/Board.py                 67     18    73%   76, 113-148, 154-155
core/Checker.py               30      8    73%   14, 35, 56-62
core/Dice.py                  29      1    97%   43
core/Player.py                 8      0   100%
core/__init__.py               0      0   100%
--------------------------------------------------------
TOTAL                        681    144    79%

```
## Pylint Report
```text
************* Module main.py
main.py:1:0: F0001: No module named main.py (fatal)
************* Module test.py
test.py:1:0: F0001: No module named test.py (fatal)

```
