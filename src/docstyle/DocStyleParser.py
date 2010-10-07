# $ANTLR 3.1.2 DocStyle.g 2010-10-07 23:40:44

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
WS=10
TAG_CLOSE=6
LETTER=7
DIGIT=9
ID=5
EOF=-1
NAMECHAR=8
TAG_OPEN=4

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TAG_OPEN", "ID", "TAG_CLOSE", "LETTER", "NAMECHAR", "DIGIT", "WS"
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
    # DocStyle.g:13:1: docString : ( tag )+ ;
    def docString(self, ):

        try:
            try:
                # DocStyle.g:13:11: ( ( tag )+ )
                # DocStyle.g:13:13: ( tag )+
                pass 
                # DocStyle.g:13:13: ( tag )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == TAG_OPEN) :
                        alt1 = 1


                    if alt1 == 1:
                        # DocStyle.g:13:13: tag
                        pass 
                        self._state.following.append(self.FOLLOW_tag_in_docString41)
                        self.tag()

                        self._state.following.pop()


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

    # $ANTLR end "docString"


    # $ANTLR start "tag"
    # DocStyle.g:15:1: tag : TAG_OPEN id= ID TAG_CLOSE ;
    def tag(self, ):

        id = None

        try:
            try:
                # DocStyle.g:15:5: ( TAG_OPEN id= ID TAG_CLOSE )
                # DocStyle.g:15:7: TAG_OPEN id= ID TAG_CLOSE
                pass 
                self.match(self.input, TAG_OPEN, self.FOLLOW_TAG_OPEN_in_tag50)
                id=self.match(self.input, ID, self.FOLLOW_ID_in_tag54)
                #action start
                print id.text
                #action end
                self.match(self.input, TAG_CLOSE, self.FOLLOW_TAG_CLOSE_in_tag58)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "tag"


    # Delegated rules


 

    FOLLOW_tag_in_docString41 = frozenset([1, 4])
    FOLLOW_TAG_OPEN_in_tag50 = frozenset([5])
    FOLLOW_ID_in_tag54 = frozenset([6])
    FOLLOW_TAG_CLOSE_in_tag58 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("DocStyleLexer", DocStyleParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
