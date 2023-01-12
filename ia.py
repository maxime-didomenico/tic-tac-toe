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
	print("im in check win")
	if tab[0][0] == 2 and tab[0][2] == 2:
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

		elif tab[1][0] == 1 and tab[1][2] == 0:
			if tab[1][2] == 0:
				tab[1][2] = 2
				tab_pos = [1,2]
				return(tab_pos)

		elif tab[1][2] == 1 and tab[1][0] == 0:
			if tab[1][0] == 0:
				tab[1][0] = 2
				tab_pos = [1,0]
				return(tab_pos)

		elif tab[2][1] == 1 and tab[0][1] == 0:
			if tab[0][1] == 0:
				tab[0][1] = 2
				tab_pos = [0,1]
				return(tab_pos)

		elif tab[2][0] == 1 and tab[0][2] == 0:
			if tab[0][2] == 0:
				tab[0][2] = 2
				tab_pos = [0,2]
				return(tab_pos)

		elif tab[0][2] == 1 and tab[2][0] == 0:
			if tab[2][0] == 0:
				tab[2][0] = 2
				tab_pos = [2,0]
				return(tab_pos)

		elif (tab[0][1] == 1 and tab[0][2] == 1) or (tab[0][1] == 1 and tab[2][0] == 1):
			if tab[2][1] == 0:
				tab[2][1] = 2
				tab_pos = [2,1]
				return(tab_pos)

		elif (tab[1][0] == 1 and tab[0][2] == 1) or (tab[1][0] == 1 and tab[2][0] == 1):
			if tab[1][2] == 0:
				tab[1][2] = 2
				tab_pos = [1,2]
				return(tab_pos)

		elif (tab[1][2] == 1 and tab[0][2] == 1) or (tab[1][2] == 1 and tab[2][0] == 1):
			if tab[1][0] == 0:
				tab[1][0] = 2
				tab_pos = [1,0]
				return(tab_pos)

		elif (tab[2][1] == 1 and tab[0][2] == 1) or (tab[2][1] == 1 and tab[2][0] == 1):
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

		elif tab[2][0] == 1:

			if tab[0][2] == 0 and tab[2][0] != 0:
				tab[0][2] = 2
				tab_pos = [0,2]
				return(tab_pos)
		
		elif tab[0][2] == 0 and tab[1][2] == 1:
			tab[0][2] = 2
			tab_pos = [0,2]
			return(tab_pos)

		elif tab[2][0] == 0 and tab[2][1] == 1:
			tab[2][0] = 2
			tab_pos = [2,0]
			return(tab_pos)

		else:
			tab_pos = draw(tab)
			return(tab_pos)


def lm_gm(tab):

	tab_pos = check_win(tab)
	return (tab_pos)

	if tab[0][0] == 2 and tab[2][0] == 2:
		if tab[1][0] == 0:
			tab[1][0] = 2
			tab_pos = [0,1]
			return(tab_pos)

	elif tab[0][0] == 2 and tab[0][2] == 2:
		if tab[0][1] == 0:
			tab[0][1] = 2
			tab_pos = [0,1]
			return(tab_pos)
		else :
			tab_pos = draw(tab)
			return (tab_pos)
	else:
		tab_pos = check_win(tab)
		return (tab_pos)