import exceptions as ex

class Action:
  def __init__(self, command, obj_phrase):
    self.command = command
    self.obj_phrase = obj_phrase

def parse(msg):
  tokens = msg.split()
  tokens_non_empty = is_empty_string(tokens)
  action = action_creator(tokens_non_empty)
  return action

def is_empty_string(str_list):
  ans = []
  for i in range(0, len(str_list)):
    if str_list[i] != "":
      ans.append(str_list[i])
  
  if len(ans) == 0:
    raise ex.EmptyCommandException("Input is empty or only contains spaces!")
  return ans

def action_creator(str_list):

  command =  str_list[0].lower()
  str_list.pop(0)
  obj_phrase = str_list

  if command == "play" and len(obj_phrase) != 0:
    return Action(command,obj_phrase)
  elif command == "player" and len(obj_phrase) == 1:
    return Action(command, obj_phrase)
  else: raise ex.MalformedCommandException("Input is not a valid command. Try again!")
