
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLOSE_PARENTHESES COMMA HYPHEN NUMBER OPEN_PARENTHESES STRING TWO_DOTSdef :  assignsassigns : assign\n               | assigns assignassign : init_graphviz contraint OPEN_PARENTHESES expr CLOSE_PARENTHESESinit_graphviz : STRING TWO_DOTScontraint : STRING HYPHEN STRING\n                 | STRING expr : componentscomponents : STRING COMMA components\n                | NUMBER COMMA components\n                | opt_case COMMA components\n                | STRING\n                | NUMBER\n                | opt_caseopt_case : STRING OPEN_PARENTHESES STRING CLOSE_PARENTHESES'
    
_lr_action_items = {'STRING':([0,2,3,4,6,9,10,11,18,19,20,21,22,],[5,5,-2,8,-3,-5,14,17,-4,14,24,14,14,]),'$end':([1,2,3,6,18,],[0,-1,-2,-3,-4,]),'TWO_DOTS':([5,],[9,]),'OPEN_PARENTHESES':([7,8,14,17,],[10,-7,20,-6,]),'HYPHEN':([8,],[11,]),'NUMBER':([10,19,21,22,],[15,15,15,15,]),'CLOSE_PARENTHESES':([12,13,14,15,16,23,24,25,26,27,],[18,-8,-12,-13,-14,-9,27,-10,-11,-15,]),'COMMA':([14,15,16,27,],[19,21,22,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'def':([0,],[1,]),'assigns':([0,],[2,]),'assign':([0,2,],[3,6,]),'init_graphviz':([0,2,],[4,4,]),'contraint':([4,],[7,]),'expr':([10,],[12,]),'components':([10,19,21,22,],[13,23,25,26,]),'opt_case':([10,19,21,22,],[16,16,16,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> def","S'",1,None,None,None),
  ('def -> assigns','def',1,'p_def_def','parser.py',56),
  ('assigns -> assign','assigns',1,'p_def_assigns','parser.py',61),
  ('assigns -> assigns assign','assigns',2,'p_def_assigns','parser.py',62),
  ('assign -> init_graphviz contraint OPEN_PARENTHESES expr CLOSE_PARENTHESES','assign',5,'p_assign','parser.py',68),
  ('init_graphviz -> STRING TWO_DOTS','init_graphviz',2,'p_init_graphviz','parser.py',72),
  ('contraint -> STRING HYPHEN STRING','contraint',3,'p_contraint','parser.py',80),
  ('contraint -> STRING','contraint',1,'p_contraint','parser.py',81),
  ('expr -> components','expr',1,'p_def_expr','parser.py',87),
  ('components -> STRING COMMA components','components',3,'p_components','parser.py',91),
  ('components -> NUMBER COMMA components','components',3,'p_components','parser.py',92),
  ('components -> opt_case COMMA components','components',3,'p_components','parser.py',93),
  ('components -> STRING','components',1,'p_components','parser.py',94),
  ('components -> NUMBER','components',1,'p_components','parser.py',95),
  ('components -> opt_case','components',1,'p_components','parser.py',96),
  ('opt_case -> STRING OPEN_PARENTHESES STRING CLOSE_PARENTHESES','opt_case',4,'p_opt_case','parser.py',104),
]