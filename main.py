def main():
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  num_words = count_words(text)
  c_dict = count_characters(text)
  
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words fournd in the document")

  sorted_chars = charts_dict_to_sorted_list(c_dict)
  for i in sorted_chars:
    print(f"The '{i['char']}' character was found {i['num']} times")
  print("--- End report ---")



def get_book_text(path):
  with open(path) as file:
    return file.read()

def count_words(book):
  words_arr = book.split()
  return len(words_arr)

def count_characters(text):
  character_dict = {}
  for i in text:
    c = i.lower()
    if not c.isalpha():
      continue 
    if c in character_dict.keys():
      character_dict[c] += 1
    else:
      character_dict[c] = 1;
  return character_dict

def sort_on(dict):
  return dict['num']

def charts_dict_to_sorted_list(dict):
  sorted = []
  for i in dict:
    sorted.append({
      'char': i,
      'num': dict[i]
    })
  sorted.sort(reverse=True, key=sort_on)
  return sorted

main()


