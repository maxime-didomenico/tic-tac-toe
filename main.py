import ia

main_tab = [[0,0,0],[0,0,0],[0,0,0]]
printed_tab = [["a","b","c"],["d","e","f"],["g","h","i"]]


def print_tab(main_tab):
    i = 0
    j = 0
    print('')
    while i < 3:
        while j < 3:
            print(main_tab[i][j], end='',)
            print(' ', end='')
            j+=1
        print('')
        i+=1
        j = 0


def check_pos():
    i = 0
    j = 0
    tab_pos = [0,0]
    print_tab(printed_tab)
    print('')
    letter = input("Choisissez un emplacement : ")
    while i < 3:
        while j < 3:
            if letter != printed_tab[i][j]:
                j+=1
            else:
                tab_pos[0] = i
                tab_pos[1] = j
                return(tab_pos)
        j = 0
        i+=1


def place_elem(tab_pos,turn):
	i = tab_pos[0]
	j = tab_pos[1]
	if (turn % 2) != 0 and main_tab[i][j] != 2:
		main_tab[i][j] = 1
		printed_tab[i][j] = "O"
	elif (turn % 2) == 0 and main_tab[i][j] != 1:
		main_tab[i][j] = 2
		printed_tab[i][j] = "X"
	else:
		print("Cette position est déjà prise, veuillez en choisir une autre : ")
		tab_pos = check_pos()
		place_elem(tab_pos,turn)


def init_game():
    player_nb = input("Combien de joueurs doit contenir cette partie ? : \n")
    if player_nb == "1":
        return 1
    elif player_nb == "2":
        return 2
    else:
        input("Je n'ai pas compris.\nCombien de joueurs participeront ?")
        init_game()


def check_win(turn):
	test = 0
	while test < 1:
		if (turn % 2) != 0:
			player = 1
			test+=1
		elif (turn % 2) == 0:
			player = 2
			test+=1
	if main_tab[0][0] == player and main_tab[0][1] == player and main_tab[0][2] == player:
		return 1
	elif main_tab[1][0] == player and main_tab[1][1] == player and main_tab[1][2] == player:
		return 1
	elif main_tab[2][0] == player and main_tab[2][1] == player and main_tab[2][2] == player:
		return 1
	elif main_tab[0][0] == player and main_tab[1][0] == player and main_tab[2][0] == player:
		return 1
	elif main_tab[0][1] == player and main_tab[1][1] == player and main_tab[2][1] == player:
		return 1
	elif main_tab[0][2] == player and main_tab[1][2] == player and main_tab[2][2] == player:
		return 1
	elif main_tab[0][0] == player and main_tab[1][1] == player and main_tab[2][2] == player:
		return 1
	elif main_tab[0][2] == player and main_tab[1][1] == player and main_tab[2][0] == player:
		return 1
	else:
		return 0


def reset():
	main_tab = [[0,0,0],[0,0,0],[0,0,0]]


def main():
	player_nbr = init_game()
	turn = 0
	tab_pos = [0,0]
	if player_nbr == 1:
		print('')
		difficulty = input("Quelle difficultée souhaitez-vous affronter ?\na) Melvin tier (très facile)\nb) Maxime tier (god mod)\n")

		#################### IA VS HU #########################

	if player_nbr == 1 and difficulty == "a":
		move = 0
		while turn < 9:
			if (turn % 2) != 0:
				tab_pos = check_pos()
				place_elem(tab_pos,turn)
				print("\n","--------------------------------------------------")
				game = check_win(turn)

			else :
				if (turn % 2 == 0):
					tab_pos = ia.draw(main_tab)
					place_elem(tab_pos,turn)
					move+=1

			game = check_win(turn)
			if game == 1: 
				if (turn % 2) != 0:
					print('')
					print("Les O gagnent.")
					print('')
					print_tab(printed_tab)

				elif (turn % 2) == 0:
					print('')
					print("Les X gagnent.")
					print('')
					print_tab(printed_tab)
					print('')

				turn = 9

			else:
				if turn == 8:
					print('')
					print("Egalite, dommage.")
					print_tab(printed_tab)
					print('')
					break

				else :
					turn+=1

	if player_nbr == 1 and difficulty == "b":
		move = 0
		while turn < 9:
			if (turn % 2) != 0:
				tab_pos = check_pos()
				place_elem(tab_pos,turn)
				print("\n","--------------------------------------------------")
				game = check_win(turn)

			elif (turn % 2) == 0:
				if (turn % 2 == 0):
					if move == 0:
						tab_pos = ia.fp_gm(main_tab)
						place_elem(tab_pos,turn)
						move+=1

					elif move == 1:
						tab_pos = ia.sp_gm(main_tab)
						place_elem(tab_pos,turn)
						move+=1

					elif move == 2:
						tab_pos = ia.tp_gm(main_tab)
						place_elem(tab_pos,turn)
						move+=1

					elif move >= 2 and move < 4:
						tab_pos = ia.lm_gm(main_tab)
						place_elem(tab_pos,turn)
						move+=1

					else:
						tab_pos = ia.draw(main_tab)
						place_elem(tab_pos,turn)
						move+=1

			game = check_win(turn)
			if game == 1: 
				if (turn % 2) != 0:
					print('')
					print("Les O gagnent.")
					print('')
					print_tab(printed_tab)

				elif (turn % 2) == 0:
					print('')
					print("Les X gagnent.")
					print('')
					print_tab(printed_tab)
					print('')

				turn = 9

			else:
				if turn == 8:
					print('')
					print("Egalite, dommage.")
					print_tab(printed_tab)
					print('')
					break

				else :
					turn+=1

		#################### HU VS HU #########################

	if player_nbr == 2:
		while turn < 9:
			if (turn % 2) != 0:
				print('\n',"Au tour des O.")
			elif (turn % 2) == 0:
				print('\n',"Au tour des X.")
			tab_pos = check_pos()
			place_elem(tab_pos,turn)
			print("\n","--------------------------------------------------")
			game = check_win(turn)
			if game == 1: 
				if (turn % 2) != 0:
					print('')
					print("Les O gagnent.")
				elif (turn % 2) == 0:
					print('')
					print("Les X gagnent.")
				turn = 9
			else:
				if turn == 8:
					print('')
					print("Egalite, dommage.\n")
					break
				else :
					turn+=1

main()