def check_turn(tab):
	i = 0
	j = 0
	count = 0
	while i < 3:
		while j < 3:
			if tab[i][j] == 1 or tab[i][j] == 2:
				count += 1
				j+=1
			else:
				j+=1
		i+=1
		j = 0
	return count

def draw(tab):
		i = 0
		j = 0
		while i < 3:
			while j < 3:
				if tab[i][j] == 0:
					tab[i][j] = 2
					tab_pos = [i,j]
					return(tab_pos)
				j+=1
			j = 0
			i+=1

def check_win(tab):
	if tab[0][0] == 2 and tab[0][2] == 2:
		print("je suis la 1")
		if tab[0][1] == 0:
			tab[0][1] = 2
			tab_pos = [0,1]
			return(tab_pos)
	if tab[0][0] == 2 and tab[2][0] == 2:
		if tab[1][0] == 0:
			tab[1][0] = 2
			tab_pos = [1,0]
			return(tab_pos)
	if tab[2][2] == 2 and tab[0][2] == 2:
		if tab[1][2] == 0:
			tab[1][2] = 2
			tab_pos = [1,2]
			return(tab_pos)
	if tab[2][2] == 2 and tab[2][0] == 2:
		if tab[2][1] == 0:
			tab[2][1] = 2
			tab_pos = [2,1]
			return(tab_pos)
	else:
		tab_pos = tp_gm(tab)
		return(tab_pos)

def fp_gm(tab):
	tab[0][0] = 2
	tab_pos = [0,0]
	return(tab_pos)

def sp_gm(tab):
	if tab[2][2] != 1:
		tab[2][2] = 2
		tab_pos = [2,2]
		return(tab_pos)
	else:
		tab[1][1] = 2
		tab_pos = [1,1]
		return(tab_pos)

def tp_gm(tab):

	if tab[2][0] == 1:
		if tab[2][2] == 1:
			tab[2][1] = 2
			tab_pos = [2,1]
			return(tab_pos)
	
	if tab[0][2] == 1:
		if tab[2][2] == 1:
			tab[1][2] = 2
			tab_pos = [1,2]
			return(tab_pos)

	if tab[1][1] == 0:
		tab[1][1] = 2
		tab_pos = [1,1]
		return(tab_pos)

	if tab[1][1] == 1:
		if tab[0][1] == 1 and tab[2][1] == 0:
			if tab[2][1] == 0:
				tab[2][1] = 2
				tab_pos = [2,1]
				return(tab_pos)

		if tab[1][0] == 1 and tab[1][2] == 0:
			if tab[1][2] == 0:
				tab[1][2] = 2
				tab_pos = [1,2]
				return(tab_pos)

		if tab[1][2] == 1 and tab[1][0] == 0:
			if tab[1][0] == 0:
				tab[1][0] = 2
				tab_pos = [1,0]
				return(tab_pos)

		if tab[2][1] == 1 and tab[0][1] == 0:
			if tab[0][1] == 0:
				tab[0][1] = 2
				tab_pos = [0,1]
				return(tab_pos)

		if tab[2][0] == 1 and tab[0][2] == 0:
			if tab[0][2] == 0:
				tab[0][2] = 2
				tab_pos = [0,2]
				return(tab_pos)

		if tab[0][2] == 1 and tab[2][0] == 0:
			if tab[2][0] == 0:
				tab[2][0] = 2
				tab_pos = [2,0]
				return(tab_pos)

		if (tab[0][1] == 1 and tab[0][2] == 1) or (tab[0][1] == 1 and tab[2][0] == 1):
			if tab[2][1] == 0:
				tab[2][1] = 2
				tab_pos = [2,1]
				return(tab_pos)

		if (tab[1][0] == 1 and tab[0][2] == 1) or (tab[1][0] == 1 and tab[2][0] == 1):
			if tab[1][2] == 0:
				tab[1][2] = 2
				tab_pos = [1,2]
				return(tab_pos)

		if (tab[1][2] == 1 and tab[0][2] == 1) or (tab[1][2] == 1 and tab[2][0] == 1):
			if tab[1][0] == 0:
				tab[1][0] = 2
				tab_pos = [1,0]
				return(tab_pos)

		if (tab[2][1] == 1 and tab[0][2] == 1) or (tab[2][1] == 1 and tab[2][0] == 1):
			if tab[0][1] == 0:
				tab[0][1] = 2
				tab_pos = [0,1]
				return(tab_pos)

	else:
		if tab[0][2] == 1:
			if tab[2][0] == 0:
				tab[2][0] = 2
				tab_pos = [2,0]
				return(tab_pos)

		if tab[2][0] == 1:

			if tab[0][2] == 0 and tab[2][0] != 0:
				tab[0][2] = 2
				tab_pos = [0,2]
				return(tab_pos)
		
		if tab[0][2] == 0 and tab[1][2] == 1:
			tab[0][2] = 2
			tab_pos = [0,2]
			return(tab_pos)

		if tab[2][0] == 0 and tab[2][1] == 1:
			tab[2][0] = 2
			tab_pos = [2,0]
			return(tab_pos)

		else:
			tab_pos = draw(tab)
			return(tab_pos)


def lm_gm(tab):

	tab_pos = check_win(tab)
	return (tab_pos)

def ia(tab, sign):
	turn = check_turn(tab)
	print("turn = ",turn)
	if turn == 0:
		return fp_gm(tab)

	elif turn == 2:
		return sp_gm(tab)

	elif turn == 4:
		return tp_gm(tab)

	elif turn >= 4 and turn <= 6:
		return lm_gm(tab)

	else:
		return draw(tab)