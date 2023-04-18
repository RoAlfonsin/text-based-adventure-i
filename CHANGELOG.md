# CHANGELOG

##04/14/2023
1. Created turn settup
2. Created is_alive function
3. Deffined battle
4. Deffined action_attack
5. Had first battle
6. commit

##04/15/2023
1. Fixed .gitignore file
2. commit ddbe6ea

3. Created CHANGELOG.md file
4. Added item lists to Warrior
5. Added comments to Item and type information
6. Created function equip_item for Warrior
7. commit ee962bf

8. First battle using an Item.
9. Defined turn function (needs work).
10. Changed bag_item_list to bag_items and forced Item class
11. Defined bag_items_print function
12. commit 806f736

13. Defined select_items for Warrior
14. Fixed bug when defense high in action_attack in setup_classes.py
15. commit f6302d8

16. Defined remove_items for Warrior
17. Added select_items and remove_items to turn in turn_settup.py
18. commit 39f9dce

##04/16/2023

1. Created new branch gear-functions
2. Created gear_bag and defined add_to_gear_bag for Warrior
3. Defined print_gear_bar for Warrior
4. commit gear-functions b4aeef5

5. Defined equip_gear for Warrior
6. Defined select_gear for Warrior
7. Added select_gear to turn in turn_settup.py
8. Changed inmunity to -1
9. Merged gear-functions with main
10. Deleted gear-functions
11. commit main 8275b54

12. Created first-campaign branch
13. Modified order of __init__ for Gear
14. Created easy_campaign_gear
15. commit first-campaign 570fa74

16. Added csv import in main
17. Changed Gear data input
18. Created gear to unlock
19. commit first-campaign 36d4ec9

20. Deffined repr for Gear 
21. Fixed print_gear_bag
22. commit first-campaign 43b8822

23. Branch created 1-create-easy_campaign_monsters
24. Changed order of input in init for Warrior
25. Created monsters csv
26. Added monsters to monsters_to_battle
27. commit and merge branches

28. Branched to solve monster_print
29. Defined monster_print for Warrior
30. Commit
31. Created testing branch for monster_print
32. Commit C2e0ff5
33. Merge

## 04/17/23

1. Created branch for issue 7 define player_print
2. Defined player_print
3. merge and commit
4. Deleted branch

5. Created branch for issue #2: easy_campaign_items
6. Created easy_campaign_items.csv file
7. Changed order of entry in init for Item
8. Recorded info for items for easy_campaign
9. Added items to bag
10. merge, commit and delete branch 5317511

11. Created branch for issue #3: add-time-to-battles
12. Added time to battle in turn_settup.py
13. Tested time in battle
14. merge, commit and delete branch

15. Created branch to solve issue #9: buff character after battle
16. Defined buff_stats
17. Added buff_stats to turn
18. Changed first_player stats
19. merge, commit and delete branch d594e03

20. Created branch to solve issue #4: Create high score file
21. Created high score file
22. Imported time and created startingtime
23. Added Congratulation message for winning the game
24. Created funcionts necesary to keep and print scores
25. merge, commit and delete branch

26. Fixed issues #10 and #11
27. Commit 

27. Fixed issue #14 by clearing equipped_item_list in remove_items
28. Commit & merge

29. Created branch for issue #13 unlock_gear
30. Added two new gear
31. Created function to add gear
32. commit, merge and erased

33. Created branch for issue #15 problems printing bag of items
34. Fixed bug printing "Health Items" when empty
35. commit, merge and erased branch

36. Created branch for issue #12 negative numbers on death
37. Fixed bug adding lines to battle method
38. commit, merge and erase branch

39. Buffed gear by 1.5 for positives
40. Buffed items by manual
41. Lowered monsters 5 to 10 by 0.8
42. commit

##04/18/23

01. Created branch to fix issue #18
02. Added prints for player stats after selecting gear and items
03. Fixed issue #18
04. Commit, merge and erase branch

05. Maxed player hp at 250 and lowered player stats

06. Fixed bug with player hp over 250
07. commit

08. Created branch to fix issue #19
09. Changed import of time for datetime
10. Added datetime.now() for start and end
11. Created and int for score
12. Recorded first high score
13. commit, merge and delete branch