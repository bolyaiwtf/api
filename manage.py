import sys, json

def load_wtfs():
  with open('content.json', encoding='utf8') as content:
    return json.load(content)

def add_entry():
  header = input('Provide a header: ')
  comment = input('Provide a comment (optional): ')

  wtfs = load_wtfs()
  last_idx = wtfs[-1]['id']

  entry = {
    'id': last_idx + 1,
    'header': header
  }

  if comment and len(comment) > 0:
    entry['comment'] = comment

  wtfs.append(entry)

  with open('content.json', 'w', encoding='utf8') as content:
    content.write(json.dumps(wtfs))
    print('Done!')

if len(sys.argv) == 1:
  print('Please provide an action.')
  exit()

def edit_entry(id):
  print('Not implemented yet.')

def delete_entry(id):
  wtfs = load_wtfs()
  matches = [x for x in wtfs if x['id'] == id]
  if len(matches) == 0:
    print('Record does not exist.')
    exit()

  wtfs.remove(matches[0])

  with open('content.json', 'w', encoding='utf8') as content:
    content.write(json.dumps(wtfs))
    print('Done!')

action = sys.argv[1]

if action not in [ 'new', 'edit', 'delete' ]:
  print('Unknown action.')
  exit()

if action == 'new':
  add_entry()

if action == 'edit':
  if len(sys.argv) < 3:
    print('Please provide an ID.')
    exit()

  id = sys.argv[2]
  edit_entry(id)

if action == 'delete':
  if len(sys.argv) < 3:
    print('Please provide an ID.')
    exit()

  id = int(sys.argv[2])
  delete_entry(id)
