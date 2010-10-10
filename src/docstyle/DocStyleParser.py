# $ANTLR 3.1.2 DocStyle.g 2010-10-10 22:42:43

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
OTHER_CHAR=8
TAG_CLOSE=11
LETTER=13
T__21=21
T__20=20
ID=9
EOF=-1
TAG_OPEN=10
NAMECHAR=14
WORD=6
T__19=19
LINE_BREAK=4
WS=16
T__18=18
T__17=17
SENTENCE=5
DIGIT=15
DOT=7
NO_LINE_BREAK=12

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "LINE_BREAK", "SENTENCE", "WORD", "DOT", "OTHER_CHAR", "ID", "TAG_OPEN", 
    "TAG_CLOSE", "NO_LINE_BREAK", "LETTER", "NAMECHAR", "DIGIT", "WS", "'@type '", 
    "': '", "'@param '", "'@return: '", "'None'"
]




class DocStyleParser(Parser):
    grammarFileName = "DocStyle.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)







                


        



    # $ANTLR start "docString"
    # DocStyle.g:15:1: docString : head tag_sections EOF ;
    def docString(self, ):

        try:
            try:
                # DocStyle.g:15:11: ( head tag_sections EOF )
                # DocStyle.g:15:13: head tag_sections EOF
                pass 
                self._state.following.append(self.FOLLOW_head_in_docString39)
                self.head()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_tag_sections_in_docString41)
                self.tag_sections()

                self._state.following.pop()
                self.match(self.input, EOF, self.FOLLOW_EOF_in_docString43)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "docString"


    # $ANTLR start "head"
    # DocStyle.g:17:1: head : LINE_BREAK description LINE_BREAK ;
    def head(self, ):

        try:
            try:
                # DocStyle.g:17:5: ( LINE_BREAK description LINE_BREAK )
                # DocStyle.g:17:7: LINE_BREAK description LINE_BREAK
                pass 
                self.match(self.input, LINE_BREAK, self.FOLLOW_LINE_BREAK_in_head50)
                self._state.following.append(self.FOLLOW_description_in_head52)
                self.description()

                self._state.following.pop()
                self.match(self.input, LINE_BREAK, self.FOLLOW_LINE_BREAK_in_head54)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "head"


    # $ANTLR start "description"
    # DocStyle.g:19:1: description : (s= SENTENCE )+ ;
    def description(self, ):

        s = None

        try:
            try:
                # DocStyle.g:20:5: ( (s= SENTENCE )+ )
                # DocStyle.g:20:7: (s= SENTENCE )+
                pass 
                # DocStyle.g:20:7: (s= SENTENCE )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == SENTENCE) :
                        alt1 = 1


                    if alt1 == 1:
                        # DocStyle.g:20:8: s= SENTENCE
                        pass 
                        s=self.match(self.input, SENTENCE, self.FOLLOW_SENTENCE_in_description70)
                        #action start
                        print 'sentence is |' + s.text + '|'
                        #action end


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "description"


    # $ANTLR start "tag_sections"
    # DocStyle.g:27:1: tag_sections : ( param_section )? return_section ;
    def tag_sections(self, ):

        try:
            try:
                # DocStyle.g:28:5: ( ( param_section )? return_section )
                # DocStyle.g:28:24: ( param_section )? return_section
                pass 
                # DocStyle.g:28:24: ( param_section )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == LINE_BREAK) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 17) :
                        alt2 = 1
                if alt2 == 1:
                    # DocStyle.g:28:24: param_section
                    pass 
                    self._state.following.append(self.FOLLOW_param_section_in_tag_sections122)
                    self.param_section()

                    self._state.following.pop()



                self._state.following.append(self.FOLLOW_return_section_in_tag_sections125)
                self.return_section()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "tag_sections"


    # $ANTLR start "param_section"
    # DocStyle.g:32:1: param_section : LINE_BREAK ( tag_type LINE_BREAK tag_param )+ LINE_BREAK ;
    def param_section(self, ):

        try:
            try:
                # DocStyle.g:33:5: ( LINE_BREAK ( tag_type LINE_BREAK tag_param )+ LINE_BREAK )
                # DocStyle.g:33:7: LINE_BREAK ( tag_type LINE_BREAK tag_param )+ LINE_BREAK
                pass 
                self.match(self.input, LINE_BREAK, self.FOLLOW_LINE_BREAK_in_param_section147)
                # DocStyle.g:33:18: ( tag_type LINE_BREAK tag_param )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 17) :
                        alt3 = 1


                    if alt3 == 1:
                        # DocStyle.g:33:19: tag_type LINE_BREAK tag_param
                        pass 
                        self._state.following.append(self.FOLLOW_tag_type_in_param_section150)
                        self.tag_type()

                        self._state.following.pop()
                        self.match(self.input, LINE_BREAK, self.FOLLOW_LINE_BREAK_in_param_section152)
                        self._state.following.append(self.FOLLOW_tag_param_in_param_section154)
                        self.tag_param()

                        self._state.following.pop()


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                self.match(self.input, LINE_BREAK, self.FOLLOW_LINE_BREAK_in_param_section158)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "param_section"


    # $ANTLR start "tag_type"
    # DocStyle.g:36:1: tag_type : '@type ' paramName= ID ': ' typeName= ID ;
    def tag_type(self, ):

        paramName = None
        typeName = None

        try:
            try:
                # DocStyle.g:37:5: ( '@type ' paramName= ID ': ' typeName= ID )
                # DocStyle.g:37:7: '@type ' paramName= ID ': ' typeName= ID
                pass 
                self.match(self.input, 17, self.FOLLOW_17_in_tag_type176)
                paramName=self.match(self.input, ID, self.FOLLOW_ID_in_tag_type180)
                self.match(self.input, 18, self.FOLLOW_18_in_tag_type182)
                typeName=self.match(self.input, ID, self.FOLLOW_ID_in_tag_type186)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "tag_type"


    # $ANTLR start "tag_param"
    # DocStyle.g:40:1: tag_param : '@param ' paramName= ID ': ' desc= description ;
    def tag_param(self, ):

        paramName = None

        try:
            try:
                # DocStyle.g:41:5: ( '@param ' paramName= ID ': ' desc= description )
                # DocStyle.g:41:7: '@param ' paramName= ID ': ' desc= description
                pass 
                self.match(self.input, 19, self.FOLLOW_19_in_tag_param203)
                paramName=self.match(self.input, ID, self.FOLLOW_ID_in_tag_param207)
                self.match(self.input, 18, self.FOLLOW_18_in_tag_param209)
                self._state.following.append(self.FOLLOW_description_in_tag_param213)
                self.description()

                self._state.following.pop()




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "tag_param"


    # $ANTLR start "return_section"
    # DocStyle.g:44:1: return_section : LINE_BREAK '@return: ' ( 'None' | description ) LINE_BREAK ;
    def return_section(self, ):

        try:
            try:
                # DocStyle.g:45:5: ( LINE_BREAK '@return: ' ( 'None' | description ) LINE_BREAK )
                # DocStyle.g:45:7: LINE_BREAK '@return: ' ( 'None' | description ) LINE_BREAK
                pass 
                self.match(self.input, LINE_BREAK, self.FOLLOW_LINE_BREAK_in_return_section230)
                self.match(self.input, 20, self.FOLLOW_20_in_return_section232)
                # DocStyle.g:45:30: ( 'None' | description )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 21) :
                    alt4 = 1
                elif (LA4_0 == SENTENCE) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # DocStyle.g:45:31: 'None'
                    pass 
                    self.match(self.input, 21, self.FOLLOW_21_in_return_section235)
                    #action start
                    print 'None'
                    #action end


                elif alt4 == 2:
                    # DocStyle.g:45:55: description
                    pass 
                    self._state.following.append(self.FOLLOW_description_in_return_section241)
                    self.description()

                    self._state.following.pop()



                self.match(self.input, LINE_BREAK, self.FOLLOW_LINE_BREAK_in_return_section244)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "return_section"


    # $ANTLR start "tag"
    # DocStyle.g:48:1: tag : TAG_OPEN id= ID TAG_CLOSE ( NO_LINE_BREAK )* LINE_BREAK ;
    def tag(self, ):

        id = None

        try:
            try:
                # DocStyle.g:49:5: ( TAG_OPEN id= ID TAG_CLOSE ( NO_LINE_BREAK )* LINE_BREAK )
                # DocStyle.g:49:7: TAG_OPEN id= ID TAG_CLOSE ( NO_LINE_BREAK )* LINE_BREAK
                pass 
                self.match(self.input, TAG_OPEN, self.FOLLOW_TAG_OPEN_in_tag262)
                id=self.match(self.input, ID, self.FOLLOW_ID_in_tag266)
                #action start
                print id.type;print id.text
                #action end
                self.match(self.input, TAG_CLOSE, self.FOLLOW_TAG_CLOSE_in_tag270)
                # DocStyle.g:49:64: ( NO_LINE_BREAK )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == NO_LINE_BREAK) :
                        alt5 = 1


                    if alt5 == 1:
                        # DocStyle.g:49:64: NO_LINE_BREAK
                        pass 
                        self.match(self.input, NO_LINE_BREAK, self.FOLLOW_NO_LINE_BREAK_in_tag272)


                    else:
                        break #loop5


                self.match(self.input, LINE_BREAK, self.FOLLOW_LINE_BREAK_in_tag275)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "tag"


    # Delegated rules


 

    FOLLOW_head_in_docString39 = frozenset([4])
    FOLLOW_tag_sections_in_docString41 = frozenset([])
    FOLLOW_EOF_in_docString43 = frozenset([1])
    FOLLOW_LINE_BREAK_in_head50 = frozenset([5])
    FOLLOW_description_in_head52 = frozenset([4])
    FOLLOW_LINE_BREAK_in_head54 = frozenset([1])
    FOLLOW_SENTENCE_in_description70 = frozenset([1, 5])
    FOLLOW_param_section_in_tag_sections122 = frozenset([4])
    FOLLOW_return_section_in_tag_sections125 = frozenset([1])
    FOLLOW_LINE_BREAK_in_param_section147 = frozenset([17])
    FOLLOW_tag_type_in_param_section150 = frozenset([4])
    FOLLOW_LINE_BREAK_in_param_section152 = frozenset([19])
    FOLLOW_tag_param_in_param_section154 = frozenset([4, 17])
    FOLLOW_LINE_BREAK_in_param_section158 = frozenset([1])
    FOLLOW_17_in_tag_type176 = frozenset([9])
    FOLLOW_ID_in_tag_type180 = frozenset([18])
    FOLLOW_18_in_tag_type182 = frozenset([9])
    FOLLOW_ID_in_tag_type186 = frozenset([1])
    FOLLOW_19_in_tag_param203 = frozenset([9])
    FOLLOW_ID_in_tag_param207 = frozenset([18])
    FOLLOW_18_in_tag_param209 = frozenset([5])
    FOLLOW_description_in_tag_param213 = frozenset([1])
    FOLLOW_LINE_BREAK_in_return_section230 = frozenset([20])
    FOLLOW_20_in_return_section232 = frozenset([5, 21])
    FOLLOW_21_in_return_section235 = frozenset([4])
    FOLLOW_description_in_return_section241 = frozenset([4])
    FOLLOW_LINE_BREAK_in_return_section244 = frozenset([1])
    FOLLOW_TAG_OPEN_in_tag262 = frozenset([9])
    FOLLOW_ID_in_tag266 = frozenset([11])
    FOLLOW_TAG_CLOSE_in_tag270 = frozenset([4, 12])
    FOLLOW_NO_LINE_BREAK_in_tag272 = frozenset([4, 12])
    FOLLOW_LINE_BREAK_in_tag275 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("DocStyleLexer", DocStyleParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
