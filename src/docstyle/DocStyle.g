grammar DocStyle;

options {
  language=Python;
  k=5;
  //backtrack=true;
}

@lexer::members {
    tagMode = True
}

docString : tag+;

tag : TAG_OPEN id=ID {print $id.text} TAG_CLOSE; 

TAG_OPEN : '@' { self.tagMode = True } ;

TAG_CLOSE : ':' { self.tagMode = False } ;

ID : {self.tagMode}?=> (LETTER | '_') (NAMECHAR)* ;


fragment NAMECHAR
    : LETTER | DIGIT | '.' | '-' | '_'
    ;

fragment DIGIT
    :    '0'..'9'
    ;

fragment LETTER
    : 'a'..'z'
    | 'A'..'Z'
    ;

WS  :  {self.tagMode}?=>
       (' '|'\r'|'\t'|'\u000C'|'\n') {channel=99;}
    ;
