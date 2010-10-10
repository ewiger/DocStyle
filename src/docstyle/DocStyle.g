grammar DocStyle;

options {
  language=Python;
  //k=5;
  //backtrack=true;
}

@lexer::members {
    tagMode = False
}

//docString : (s=sentence {print 'sentence is |' + $s.text + '|'})+ EOF;
//docString : head ({print 'tag'} tag description)+ EOF;
docString : head tag_sections EOF;

head: LINE_BREAK description LINE_BREAK;

description 
    : (s=SENTENCE {print 'sentence is |' + $s.text + '|'})+
    ;

SENTENCE : WORD (' '+ WORD)+ DOT;

WORD: (OTHER_CHAR )+;

tag_sections
    : /*etc_section?*/ param_section? return_section
    ;
    

param_section
    : LINE_BREAK (tag_type LINE_BREAK tag_param)+ LINE_BREAK 
    ;

tag_type
    : '@type ' paramName=ID ': ' typeName=ID
    ;

tag_param
    : '@param ' paramName=ID ': ' desc=description
    ;

return_section
    : LINE_BREAK '@return: ' ('None' {print 'None'} | description) LINE_BREAK
    ;

tag 
    : TAG_OPEN id=ID {print $id.type;print $id.text} TAG_CLOSE NO_LINE_BREAK* LINE_BREAK
    ; 

/*
WORD : (WORDCHAR)*;

fragment WORDCHAR
    : LETTER | DIGIT | '-' | '_'
    ;
*/

// Sentence lexing

DOT 
    : '.'
    ;


// Type tag

// TODO: put here builtin python types

// Unknown tag
TAG_OPEN 
    : '@' { self.tagMode = True }    
    ;

TAG_CLOSE 
    : {self.tagMode}?=> 
      ':' { self.tagMode = False } 
    ;

ID 
    : {self.tagMode}?=> 
      {print 'ID'}
      (LETTER | '_') (NAMECHAR)* 
    ;

fragment NAMECHAR
    : {self.tagMode}?=> 
      LETTER | DIGIT | DOT | '-' | '_'
    ;

fragment DIGIT
    : {self.tagMode}?=> 
         '0'..'9'
    ;

fragment LETTER
    : {self.tagMode}?=> 
      'a'..'z'
    | 'A'..'Z'
    ;

// Common lexing

LINE_BREAK
    :  ('\r'? '\n') //{$channel=HIDDEN;}
    ;

WS  
    :  (' '|'\t'|'\u000C') {$channel=HIDDEN;}
    ;

fragment OTHER_CHAR
    :    ~('@'|'.'|' '|'\t'|'\u000C'|'\r'|'\n')
    ;

fragment NO_LINE_BREAK
    :    ~('\r'|'\n')
    ;

