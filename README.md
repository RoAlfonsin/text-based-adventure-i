# text-based-adventure-i

Text-based-adventure-i is a text-based adventure game written in python

## Features
- 15 plus gear items
- 3  consumable item types
- 15 monsters to battle
- Score keeping
- Simple commands

## How to play
- At the beginning of every turn, the stats for the player and the monster will be printed.
- The player selects one gear item to use during battle. This item can be used for as many battles as the user wants.
- The player selects the consumable items for the battle. These items can only be used for one battle.
- The battle will occur.
- If the player is alive at the end of battle, a +30 health bonus will be awarded. The player hp points are capped at 250.
- The player will select to increase either the attack stat or defense stat by 10 point.
- A new turn will begin by printing the stats of player and monster.

## Battle
- On every battle, the player, and the monster exchange attacks in the following order.
1. If the player is alive, it attacks.
2. If the monster is alive, it attacks.
- Battle damage is calculated by subtracting the attack stat of the attacker from the defense stat of the defender.
- If the attack stat is lower than the defense stat the defender will receive 1 point of damage.