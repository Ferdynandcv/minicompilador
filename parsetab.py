
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'APOSTROPHE CADENA COMA COMENTARIOS DIVIDIR DO DOSPUNTOS ELSE FALSE FOR FUNCION HASHTAG ID IF IGUAL IGUALXDOS LBLOCK LPAREN MAS MASXDOS MAYOR MAYORIGUALQ MENOR MENORIGUALQ MENOS MULT NUMERO PRINT PUNTOCOMA QUOTES RBLOCK RPAREN TRUE VAR WHILEprograma : FUNCION ID LPAREN RPAREN LBLOCK declaracionLista RBLOCKdeclaracionLista : declaracionLista  declaration\n                                            | declaration\n    declaration : tipo ID PUNTOCOMA\n                    | ID IGUAL var PUNTOCOMA\n                    | tipo ID IGUAL var PUNTOCOMA\n                    | if_condicion\n                    | var PUNTOCOMA\n                    | do_condicion\n                    | while_condition\n    declaration : tipo ID IGUAL expression PUNTOCOMA\n                  | ID IGUAL expression PUNTOCOMA\n                  | tipo ID IGUAL expression_avanced PUNTOCOMA\n                  | ID IGUAL expression_avanced PUNTOCOMA\n    expression : var MAS var\n                  | var MENOS var\n                  | var  MULT var\n                  | var DIVIDIR var\n    expression_avanced : var MAS LPAREN  expression RPAREN\n                   | var MENOS LPAREN  expression RPAREN\n                   | var  MULT LPAREN  expression RPAREN\n                   | var DIVIDIR LPAREN  expression RPAREN\n     expression_bool : var IGUALXDOS var\n                   | var MENOR var\n                   | var MAYOR var\n                   | var MAYORIGUALQ var\n                   | var MENORIGUALQ var\n     if_condicion : IF LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK\n                | IF LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK ELSE LBLOCK declaracionLista RBLOCK\n    do_condicion : DO LBLOCK declaracionLista RBLOCK WHILE LPAREN expression_bool RPAREN \n    while_condition : \n                | WHILE LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK \n    tipo : VAR\n    var : ID\n           | NUMERO\n           | CADENA\n     '
    
_lr_action_items = {'FUNCION':([0,],[2,]),'$end':([1,22,],[0,-1,]),'ID':([2,6,8,9,10,12,13,14,15,21,23,25,26,27,28,33,34,37,39,40,41,42,43,44,45,50,51,52,53,54,58,60,62,64,65,66,67,68,75,81,82,83,84,85,86,87,92,94,96,97,98,99,],[3,7,7,-3,24,-7,-9,-10,-33,29,-2,-8,29,7,29,-4,29,7,-5,29,29,29,29,-12,-14,29,29,29,29,29,29,29,29,29,-6,-11,-13,7,7,7,29,7,29,29,29,29,-28,-32,-30,7,7,-29,]),'LPAREN':([3,16,20,40,41,42,43,74,],[4,26,28,58,60,62,64,82,]),'RPAREN':([4,17,18,29,35,38,57,59,61,63,69,70,71,72,73,77,78,79,80,93,],[5,-35,-36,-34,49,56,-15,-16,-17,-18,-23,-24,-25,-26,-27,88,89,90,91,96,]),'LBLOCK':([5,19,49,56,95,],[6,27,68,75,97,]),'VAR':([6,8,9,12,13,14,23,25,27,33,37,39,44,45,65,66,67,68,75,81,83,92,94,96,97,98,99,],[15,15,-3,-7,-9,-10,-2,-8,15,-4,15,-5,-12,-14,-6,-11,-13,15,15,15,15,-28,-32,-30,15,15,-29,]),'IF':([6,8,9,12,13,14,23,25,27,33,37,39,44,45,65,66,67,68,75,81,83,92,94,96,97,98,99,],[16,16,-3,-7,-9,-10,-2,-8,16,-4,16,-5,-12,-14,-6,-11,-13,16,16,16,16,-28,-32,-30,16,16,-29,]),'NUMERO':([6,8,9,12,13,14,21,23,25,26,27,28,33,34,37,39,40,41,42,43,44,45,50,51,52,53,54,58,60,62,64,65,66,67,68,75,81,82,83,84,85,86,87,92,94,96,97,98,99,],[17,17,-3,-7,-9,-10,17,-2,-8,17,17,17,-4,17,17,-5,17,17,17,17,-12,-14,17,17,17,17,17,17,17,17,17,-6,-11,-13,17,17,17,17,17,17,17,17,17,-28,-32,-30,17,17,-29,]),'CADENA':([6,8,9,12,13,14,21,23,25,26,27,28,33,34,37,39,40,41,42,43,44,45,50,51,52,53,54,58,60,62,64,65,66,67,68,75,81,82,83,84,85,86,87,92,94,96,97,98,99,],[18,18,-3,-7,-9,-10,18,-2,-8,18,18,18,-4,18,18,-5,18,18,18,18,-12,-14,18,18,18,18,18,18,18,18,18,-6,-11,-13,18,18,18,18,18,18,18,18,18,-28,-32,-30,18,18,-29,]),'DO':([6,8,9,12,13,14,23,25,27,33,37,39,44,45,65,66,67,68,75,81,83,92,94,96,97,98,99,],[19,19,-3,-7,-9,-10,-2,-8,19,-4,19,-5,-12,-14,-6,-11,-13,19,19,19,19,-28,-32,-30,19,19,-29,]),'RBLOCK':([6,8,9,12,13,14,23,25,27,33,37,39,44,45,65,66,67,68,75,81,83,92,94,96,97,98,99,],[-31,22,-3,-7,-9,-10,-2,-8,-31,-4,55,-5,-12,-14,-6,-11,-13,-31,-31,92,94,-28,-32,-30,-31,99,-29,]),'WHILE':([6,8,9,12,13,14,23,25,27,33,37,39,44,45,55,65,66,67,68,75,81,83,92,94,96,97,98,99,],[20,20,-3,-7,-9,-10,-2,-8,20,-4,20,-5,-12,-14,74,-6,-11,-13,20,20,20,20,-28,-32,-30,20,20,-29,]),'IGUAL':([7,24,],[21,34,]),'PUNTOCOMA':([7,11,17,18,24,29,30,31,32,46,47,48,57,59,61,63,88,89,90,91,],[-34,25,-35,-36,33,-34,39,44,45,65,66,67,-15,-16,-17,-18,-19,-20,-21,-22,]),'MAS':([17,18,29,30,46,76,],[-35,-36,-34,40,40,84,]),'MENOS':([17,18,29,30,46,76,],[-35,-36,-34,41,41,85,]),'MULT':([17,18,29,30,46,76,],[-35,-36,-34,42,42,86,]),'DIVIDIR':([17,18,29,30,46,76,],[-35,-36,-34,43,43,87,]),'IGUALXDOS':([17,18,29,36,],[-35,-36,-34,50,]),'MENOR':([17,18,29,36,],[-35,-36,-34,51,]),'MAYOR':([17,18,29,36,],[-35,-36,-34,52,]),'MAYORIGUALQ':([17,18,29,36,],[-35,-36,-34,53,]),'MENORIGUALQ':([17,18,29,36,],[-35,-36,-34,54,]),'ELSE':([92,],[95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracionLista':([6,27,68,75,97,],[8,37,81,83,98,]),'declaration':([6,8,27,37,68,75,81,83,97,98,],[9,23,9,23,9,9,23,23,9,23,]),'tipo':([6,8,27,37,68,75,81,83,97,98,],[10,10,10,10,10,10,10,10,10,10,]),'var':([6,8,21,26,27,28,34,37,40,41,42,43,50,51,52,53,54,58,60,62,64,68,75,81,82,83,84,85,86,87,97,98,],[11,11,30,36,11,36,46,11,57,59,61,63,69,70,71,72,73,76,76,76,76,11,11,11,36,11,57,59,61,63,11,11,]),'if_condicion':([6,8,27,37,68,75,81,83,97,98,],[12,12,12,12,12,12,12,12,12,12,]),'do_condicion':([6,8,27,37,68,75,81,83,97,98,],[13,13,13,13,13,13,13,13,13,13,]),'while_condition':([6,8,27,37,68,75,81,83,97,98,],[14,14,14,14,14,14,14,14,14,14,]),'expression':([21,34,58,60,62,64,],[31,47,77,78,79,80,]),'expression_avanced':([21,34,],[32,48,]),'expression_bool':([26,28,82,],[35,38,93,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> FUNCION ID LPAREN RPAREN LBLOCK declaracionLista RBLOCK','programa',7,'p_programa','AnalizadorSin.py',10),
  ('declaracionLista -> declaracionLista declaration','declaracionLista',2,'p_declaracionLista','AnalizadorSin.py',14),
  ('declaracionLista -> declaration','declaracionLista',1,'p_declaracionLista','AnalizadorSin.py',15),
  ('declaration -> tipo ID PUNTOCOMA','declaration',3,'p_declaration','AnalizadorSin.py',21),
  ('declaration -> ID IGUAL var PUNTOCOMA','declaration',4,'p_declaration','AnalizadorSin.py',22),
  ('declaration -> tipo ID IGUAL var PUNTOCOMA','declaration',5,'p_declaration','AnalizadorSin.py',23),
  ('declaration -> if_condicion','declaration',1,'p_declaration','AnalizadorSin.py',24),
  ('declaration -> var PUNTOCOMA','declaration',2,'p_declaration','AnalizadorSin.py',25),
  ('declaration -> do_condicion','declaration',1,'p_declaration','AnalizadorSin.py',26),
  ('declaration -> while_condition','declaration',1,'p_declaration','AnalizadorSin.py',27),
  ('declaration -> tipo ID IGUAL expression PUNTOCOMA','declaration',5,'p_operation','AnalizadorSin.py',36),
  ('declaration -> ID IGUAL expression PUNTOCOMA','declaration',4,'p_operation','AnalizadorSin.py',37),
  ('declaration -> tipo ID IGUAL expression_avanced PUNTOCOMA','declaration',5,'p_operation','AnalizadorSin.py',38),
  ('declaration -> ID IGUAL expression_avanced PUNTOCOMA','declaration',4,'p_operation','AnalizadorSin.py',39),
  ('expression -> var MAS var','expression',3,'p_expression','AnalizadorSin.py',47),
  ('expression -> var MENOS var','expression',3,'p_expression','AnalizadorSin.py',48),
  ('expression -> var MULT var','expression',3,'p_expression','AnalizadorSin.py',49),
  ('expression -> var DIVIDIR var','expression',3,'p_expression','AnalizadorSin.py',50),
  ('expression_avanced -> var MAS LPAREN expression RPAREN','expression_avanced',5,'p_expression_avanced','AnalizadorSin.py',56),
  ('expression_avanced -> var MENOS LPAREN expression RPAREN','expression_avanced',5,'p_expression_avanced','AnalizadorSin.py',57),
  ('expression_avanced -> var MULT LPAREN expression RPAREN','expression_avanced',5,'p_expression_avanced','AnalizadorSin.py',58),
  ('expression_avanced -> var DIVIDIR LPAREN expression RPAREN','expression_avanced',5,'p_expression_avanced','AnalizadorSin.py',59),
  ('expression_bool -> var IGUALXDOS var','expression_bool',3,'p_expression_bool','AnalizadorSin.py',65),
  ('expression_bool -> var MENOR var','expression_bool',3,'p_expression_bool','AnalizadorSin.py',66),
  ('expression_bool -> var MAYOR var','expression_bool',3,'p_expression_bool','AnalizadorSin.py',67),
  ('expression_bool -> var MAYORIGUALQ var','expression_bool',3,'p_expression_bool','AnalizadorSin.py',68),
  ('expression_bool -> var MENORIGUALQ var','expression_bool',3,'p_expression_bool','AnalizadorSin.py',69),
  ('if_condicion -> IF LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK','if_condicion',7,'p_if_condicion','AnalizadorSin.py',74),
  ('if_condicion -> IF LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK ELSE LBLOCK declaracionLista RBLOCK','if_condicion',11,'p_if_condicion','AnalizadorSin.py',75),
  ('do_condicion -> DO LBLOCK declaracionLista RBLOCK WHILE LPAREN expression_bool RPAREN','do_condicion',8,'p_do_condicion','AnalizadorSin.py',81),
  ('while_condition -> <empty>','while_condition',0,'p_while_condition','AnalizadorSin.py',87),
  ('while_condition -> WHILE LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK','while_condition',7,'p_while_condition','AnalizadorSin.py',88),
  ('tipo -> VAR','tipo',1,'p_tipo','AnalizadorSin.py',94),
  ('var -> ID','var',1,'p_var','AnalizadorSin.py',100),
  ('var -> NUMERO','var',1,'p_var','AnalizadorSin.py',101),
  ('var -> CADENA','var',1,'p_var','AnalizadorSin.py',102),
]