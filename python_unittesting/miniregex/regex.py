
def match(regexp, text):
	if not regexp:
		return None
	if regexp[0] == '^':
		regexp = regexp[1:]
	m = match_head(regexp, text, '', 0)
	if not m:
		return None
	return (m[0], (0, m[1]))

def search(regexp, text):
	if not regexp:
		return True
	i = 0
	if regexp[0] == '^':
		m = match_head(regexp[1:], text, '', i)
	else:
		for i in range(len(text)):
			m = match_head(regexp, text[i:], '', i)
			if m:
				break
	if not m:
		return None
	return (m[0], (i, m[1]))

def match_head(regexp, text, matched, end):
	if (not regexp) or (regexp == '$' and not text):
		return matched, end
	if len(regexp) > 1 and regexp[1] == '*':
		if regexp[2:].startswith('?'):
			return match_star(regexp[3:], text, matched, end, regexp[0], False)
		else:
			return match_star(regexp[2:], text, matched, end, regexp[0], True)
	if text and (regexp[0] == '.' or regexp[0] == text[0]):
		return match_head(regexp[1:], text[1:], matched+text[0], end+1)
	return None

def match_star(regexp, text, matched, end, c, greedy):
	j, l = 0, len(text)
	s = ''
	while j < l:
		m = match_head(regexp, text[j:], matched+s, end+j)
		if greedy:
			if text[j] != c and c != '.':
				return m
		else:
			if m:
				return m
			elif not m and (text[j] != c and c != '.'):
				return None
		s += text[j]
		j += 1
	return matched+s, end+j

if __name__ == '__main__':
	print(match(r'ab*?', 'abbc'), 'abbc')
	print(match(r'ab*?c', 'abbc'), 'abbc')
	print(search(r'a.*?b', 'dacbd'), 'dacbd')