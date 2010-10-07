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
TAG_OPEN=4
NAMECHAR=8


class DocStyleLexer(Lexer):

    grammarFileName = "DocStyle.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)




                               
    tagMode = True



    # $ANTLR start "TAG_OPEN"
    def mTAG_OPEN(self, ):

        try:
            _type = TAG_OPEN
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:17:10: ( '@' )
            # DocStyle.g:17:12: '@'
            pass 
            self.match(64)
            #action start
            self.tagMode = True 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TAG_OPEN"



    # $ANTLR start "TAG_CLOSE"
    def mTAG_CLOSE(self, ):

        try:
            _type = TAG_CLOSE
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:19:11: ( ':' )
            # DocStyle.g:19:13: ':'
            pass 
            self.match(58)
            #action start
            self.tagMode = False 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TAG_CLOSE"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:21:4: ({...}? => ( LETTER | '_' ) ( NAMECHAR )* )
            # DocStyle.g:21:6: {...}? => ( LETTER | '_' ) ( NAMECHAR )*
            pass 
            if not ((self.tagMode)):
                raise FailedPredicateException(self.input, "ID", "self.tagMode")

            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # DocStyle.g:21:39: ( NAMECHAR )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((45 <= LA1_0 <= 46) or (48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # DocStyle.g:21:40: NAMECHAR
                    pass 
                    self.mNAMECHAR()


                else:
                    break #loop1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "NAMECHAR"
    def mNAMECHAR(self, ):

        try:
            # DocStyle.g:25:5: ( LETTER | DIGIT | '.' | '-' | '_' )
            # DocStyle.g:
            pass 
            if (45 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "NAMECHAR"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # DocStyle.g:29:5: ( '0' .. '9' )
            # DocStyle.g:29:10: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # DocStyle.g:33:5: ( 'a' .. 'z' | 'A' .. 'Z' )
            # DocStyle.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:37:5: ({...}? => ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # DocStyle.g:37:8: {...}? => ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            pass 
            if not ((self.tagMode)):
                raise FailedPredicateException(self.input, "WS", "self.tagMode")

            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            channel=99;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # DocStyle.g:1:8: ( TAG_OPEN | TAG_CLOSE | ID | WS )
        alt2 = 4
        LA2_0 = self.input.LA(1)

        if (LA2_0 == 64) :
            alt2 = 1
        elif (LA2_0 == 58) :
            alt2 = 2
        elif ((65 <= LA2_0 <= 90) or LA2_0 == 95 or (97 <= LA2_0 <= 122)) and ((self.tagMode)):
            alt2 = 3
        elif ((9 <= LA2_0 <= 10) or (12 <= LA2_0 <= 13) or LA2_0 == 32) and ((self.tagMode)):
            alt2 = 4
        else:
            nvae = NoViableAltException("", 2, 0, self.input)

            raise nvae

        if alt2 == 1:
            # DocStyle.g:1:10: TAG_OPEN
            pass 
            self.mTAG_OPEN()


        elif alt2 == 2:
            # DocStyle.g:1:19: TAG_CLOSE
            pass 
            self.mTAG_CLOSE()


        elif alt2 == 3:
            # DocStyle.g:1:29: ID
            pass 
            self.mID()


        elif alt2 == 4:
            # DocStyle.g:1:32: WS
            pass 
            self.mWS()







 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(DocStyleLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
