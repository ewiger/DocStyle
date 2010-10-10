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


class DocStyleLexer(Lexer):

    grammarFileName = "DocStyle.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )




                               
    tagMode = False



    # $ANTLR start "T__17"
    def mT__17(self, ):

        try:
            _type = T__17
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:11:7: ( '@type ' )
            # DocStyle.g:11:9: '@type '
            pass 
            self.match("@type ")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__17"



    # $ANTLR start "T__18"
    def mT__18(self, ):

        try:
            _type = T__18
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:12:7: ( ': ' )
            # DocStyle.g:12:9: ': '
            pass 
            self.match(": ")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__18"



    # $ANTLR start "T__19"
    def mT__19(self, ):

        try:
            _type = T__19
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:13:7: ( '@param ' )
            # DocStyle.g:13:9: '@param '
            pass 
            self.match("@param ")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__19"



    # $ANTLR start "T__20"
    def mT__20(self, ):

        try:
            _type = T__20
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:14:7: ( '@return: ' )
            # DocStyle.g:14:9: '@return: '
            pass 
            self.match("@return: ")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__20"



    # $ANTLR start "T__21"
    def mT__21(self, ):

        try:
            _type = T__21
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:15:7: ( 'None' )
            # DocStyle.g:15:9: 'None'
            pass 
            self.match("None")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__21"



    # $ANTLR start "SENTENCE"
    def mSENTENCE(self, ):

        try:
            _type = SENTENCE
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:23:10: ( WORD ( ( ' ' )+ WORD )+ DOT )
            # DocStyle.g:23:12: WORD ( ( ' ' )+ WORD )+ DOT
            pass 
            self.mWORD()
            # DocStyle.g:23:17: ( ( ' ' )+ WORD )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 32) :
                    alt2 = 1


                if alt2 == 1:
                    # DocStyle.g:23:18: ( ' ' )+ WORD
                    pass 
                    # DocStyle.g:23:18: ( ' ' )+
                    cnt1 = 0
                    while True: #loop1
                        alt1 = 2
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == 32) :
                            alt1 = 1


                        if alt1 == 1:
                            # DocStyle.g:23:18: ' '
                            pass 
                            self.match(32)


                        else:
                            if cnt1 >= 1:
                                break #loop1

                            eee = EarlyExitException(1, self.input)
                            raise eee

                        cnt1 += 1


                    self.mWORD()


                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1


            self.mDOT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SENTENCE"



    # $ANTLR start "WORD"
    def mWORD(self, ):

        try:
            _type = WORD
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:25:5: ( ( OTHER_CHAR )+ )
            # DocStyle.g:25:7: ( OTHER_CHAR )+
            pass 
            # DocStyle.g:25:7: ( OTHER_CHAR )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 8) or LA3_0 == 11 or (14 <= LA3_0 <= 31) or (33 <= LA3_0 <= 45) or (47 <= LA3_0 <= 63) or (65 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # DocStyle.g:25:8: OTHER_CHAR
                    pass 
                    self.mOTHER_CHAR()


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WORD"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:63:5: ( '.' )
            # DocStyle.g:63:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "TAG_OPEN"
    def mTAG_OPEN(self, ):

        try:
            _type = TAG_OPEN
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:73:5: ( '@' )
            # DocStyle.g:73:7: '@'
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

            # DocStyle.g:77:5: ({...}? => ':' )
            # DocStyle.g:77:7: {...}? => ':'
            pass 
            if not ((self.tagMode)):
                raise FailedPredicateException(self.input, "TAG_CLOSE", "self.tagMode")

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

            # DocStyle.g:82:5: ({...}? => ( LETTER | '_' ) ( NAMECHAR )* )
            # DocStyle.g:82:7: {...}? => ( LETTER | '_' ) ( NAMECHAR )*
            pass 
            if not ((self.tagMode)):
                raise FailedPredicateException(self.input, "ID", "self.tagMode")

            #action start
            print 'ID'
            #action end
            # DocStyle.g:84:7: ( LETTER | '_' )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if ((97 <= LA4_0 <= 122)) and ((self.tagMode)):
                alt4 = 1
            elif ((65 <= LA4_0 <= 90)) :
                alt4 = 1
            elif (LA4_0 == 95) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # DocStyle.g:84:8: LETTER
                pass 
                self.mLETTER()


            elif alt4 == 2:
                # DocStyle.g:84:17: '_'
                pass 
                self.match(95)



            # DocStyle.g:84:22: ( NAMECHAR )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90) or (97 <= LA5_0 <= 122)) and ((self.tagMode)):
                    alt5 = 1
                elif ((45 <= LA5_0 <= 46) or LA5_0 == 95) :
                    alt5 = 1


                if alt5 == 1:
                    # DocStyle.g:84:23: NAMECHAR
                    pass 
                    self.mNAMECHAR()


                else:
                    break #loop5





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "NAMECHAR"
    def mNAMECHAR(self, ):

        try:
            # DocStyle.g:88:5: ({...}? => LETTER | DIGIT | DOT | '-' | '_' )
            alt6 = 5
            LA6_0 = self.input.LA(1)

            if ((65 <= LA6_0 <= 90) or (97 <= LA6_0 <= 122)) and ((self.tagMode)):
                alt6 = 1
            elif ((48 <= LA6_0 <= 57)) and ((self.tagMode)):
                alt6 = 2
            elif (LA6_0 == 46) :
                alt6 = 3
            elif (LA6_0 == 45) :
                alt6 = 4
            elif (LA6_0 == 95) :
                alt6 = 5
            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae

            if alt6 == 1:
                # DocStyle.g:88:7: {...}? => LETTER
                pass 
                if not ((self.tagMode)):
                    raise FailedPredicateException(self.input, "NAMECHAR", "self.tagMode")

                self.mLETTER()


            elif alt6 == 2:
                # DocStyle.g:89:16: DIGIT
                pass 
                self.mDIGIT()


            elif alt6 == 3:
                # DocStyle.g:89:24: DOT
                pass 
                self.mDOT()


            elif alt6 == 4:
                # DocStyle.g:89:30: '-'
                pass 
                self.match(45)


            elif alt6 == 5:
                # DocStyle.g:89:36: '_'
                pass 
                self.match(95)



        finally:

            pass

    # $ANTLR end "NAMECHAR"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # DocStyle.g:93:5: ({...}? => '0' .. '9' )
            # DocStyle.g:93:7: {...}? => '0' .. '9'
            pass 
            if not ((self.tagMode)):
                raise FailedPredicateException(self.input, "DIGIT", "self.tagMode")

            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # DocStyle.g:98:5: ({...}? => 'a' .. 'z' | 'A' .. 'Z' )
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if ((97 <= LA7_0 <= 122)) and ((self.tagMode)):
                alt7 = 1
            elif ((65 <= LA7_0 <= 90)) :
                alt7 = 2
            else:
                nvae = NoViableAltException("", 7, 0, self.input)

                raise nvae

            if alt7 == 1:
                # DocStyle.g:98:7: {...}? => 'a' .. 'z'
                pass 
                if not ((self.tagMode)):
                    raise FailedPredicateException(self.input, "LETTER", "self.tagMode")

                self.matchRange(97, 122)


            elif alt7 == 2:
                # DocStyle.g:100:7: 'A' .. 'Z'
                pass 
                self.matchRange(65, 90)



        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "LINE_BREAK"
    def mLINE_BREAK(self, ):

        try:
            _type = LINE_BREAK
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:106:5: ( ( ( '\\r' )? '\\n' ) )
            # DocStyle.g:106:8: ( ( '\\r' )? '\\n' )
            pass 
            # DocStyle.g:106:8: ( ( '\\r' )? '\\n' )
            # DocStyle.g:106:9: ( '\\r' )? '\\n'
            pass 
            # DocStyle.g:106:9: ( '\\r' )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 13) :
                alt8 = 1
            if alt8 == 1:
                # DocStyle.g:106:9: '\\r'
                pass 
                self.match(13)



            self.match(10)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_BREAK"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # DocStyle.g:110:5: ( ( ' ' | '\\t' | '\\u000C' ) )
            # DocStyle.g:110:8: ( ' ' | '\\t' | '\\u000C' )
            pass 
            if self.input.LA(1) == 9 or self.input.LA(1) == 12 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "OTHER_CHAR"
    def mOTHER_CHAR(self, ):

        try:
            # DocStyle.g:114:5: (~ ( '@' | '.' | ' ' | '\\t' | '\\u000C' | '\\r' | '\\n' ) )
            # DocStyle.g:114:10: ~ ( '@' | '.' | ' ' | '\\t' | '\\u000C' | '\\r' | '\\n' )
            pass 
            if (0 <= self.input.LA(1) <= 8) or self.input.LA(1) == 11 or (14 <= self.input.LA(1) <= 31) or (33 <= self.input.LA(1) <= 45) or (47 <= self.input.LA(1) <= 63) or (65 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "OTHER_CHAR"



    # $ANTLR start "NO_LINE_BREAK"
    def mNO_LINE_BREAK(self, ):

        try:
            # DocStyle.g:118:5: (~ ( '\\r' | '\\n' ) )
            # DocStyle.g:118:10: ~ ( '\\r' | '\\n' )
            pass 
            if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "NO_LINE_BREAK"



    def mTokens(self):
        # DocStyle.g:1:8: ( T__17 | T__18 | T__19 | T__20 | T__21 | SENTENCE | WORD | DOT | TAG_OPEN | TAG_CLOSE | ID | LINE_BREAK | WS )
        alt9 = 13
        alt9 = self.dfa9.predict(self.input)
        if alt9 == 1:
            # DocStyle.g:1:10: T__17
            pass 
            self.mT__17()


        elif alt9 == 2:
            # DocStyle.g:1:16: T__18
            pass 
            self.mT__18()


        elif alt9 == 3:
            # DocStyle.g:1:22: T__19
            pass 
            self.mT__19()


        elif alt9 == 4:
            # DocStyle.g:1:28: T__20
            pass 
            self.mT__20()


        elif alt9 == 5:
            # DocStyle.g:1:34: T__21
            pass 
            self.mT__21()


        elif alt9 == 6:
            # DocStyle.g:1:40: SENTENCE
            pass 
            self.mSENTENCE()


        elif alt9 == 7:
            # DocStyle.g:1:49: WORD
            pass 
            self.mWORD()


        elif alt9 == 8:
            # DocStyle.g:1:54: DOT
            pass 
            self.mDOT()


        elif alt9 == 9:
            # DocStyle.g:1:58: TAG_OPEN
            pass 
            self.mTAG_OPEN()


        elif alt9 == 10:
            # DocStyle.g:1:67: TAG_CLOSE
            pass 
            self.mTAG_CLOSE()


        elif alt9 == 11:
            # DocStyle.g:1:77: ID
            pass 
            self.mID()


        elif alt9 == 12:
            # DocStyle.g:1:80: LINE_BREAK
            pass 
            self.mLINE_BREAK()


        elif alt9 == 13:
            # DocStyle.g:1:91: WS
            pass 
            self.mWS()







    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\1\uffff\1\16\1\20\1\22\1\32\1\uffff\1\33\1\34\1\35\6\uffff\1\36"
        u"\1\uffff\1\41\2\uffff\1\42\1\43\1\44\1\45\1\uffff\1\46\6\uffff"
        u"\1\50\6\uffff\1\51\2\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\52\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\0\1\160\3\0\1\uffff\3\0\6\uffff\4\0\1\uffff\4\0\1\uffff\4\0"
        u"\3\uffff\11\0\1\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\uffff\1\164\3\uffff\1\uffff\3\uffff\6\uffff\1\uffff\1\0\1\uffff"
        u"\1\0\1\uffff\4\uffff\1\uffff\1\uffff\3\0\3\uffff\1\uffff\6\0\1"
        u"\uffff\1\0\1\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\5\uffff\1\10\3\uffff\1\14\1\15\1\1\1\3\1\4\1\11\4\uffff\1\6\4"
        u"\uffff\1\13\4\uffff\1\7\1\2\1\12\11\uffff\1\5"
        )

    DFA9_special = DFA.unpack(
        u"\1\33\1\uffff\1\24\1\32\1\17\1\uffff\1\23\1\25\1\0\6\uffff\1\22"
        u"\1\4\1\27\1\20\1\uffff\1\21\1\2\1\3\1\30\1\uffff\1\26\1\16\1\15"
        u"\1\14\3\uffff\1\31\1\13\1\12\1\11\1\10\1\7\1\6\1\1\1\5\1\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\11\10\1\12\1\11\1\10\1\12\1\11\22\10\1\12\15\10\1\5"
        u"\13\10\1\2\5\10\1\1\15\6\1\3\14\6\4\10\1\7\1\10\32\4\uff85\10"),
        DFA.unpack(u"\1\14\1\uffff\1\15\1\uffff\1\13"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\17\15\10\1\uffff"
        u"\21\10\1\uffff\uffbf\10"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\16\24\1\21\13"
        u"\24\uff85\10"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\15\10\1\uffff"
        u"\21\10\1\uffff\uffbf\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\11\23\2\uffff\1\23\2\uffff\40\23\1\uffff\21\23\1\uffff"
        u"\uffbf\23"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\15\24\1\40\14"
        u"\24\uff85\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\4\24\1\47\25\24"
        u"\uff85\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\11\10\2\uffff\1\10\2\uffff\22\10\1\23\14\10\1\27\1"
        u"\30\1\10\12\26\6\10\1\uffff\32\25\4\10\1\31\1\10\32\24\uff85\10"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA9_8 = input.LA(1)

                s = -1
                if (LA9_8 == 32):
                    s = 19

                elif ((0 <= LA9_8 <= 8) or LA9_8 == 11 or (14 <= LA9_8 <= 31) or (33 <= LA9_8 <= 45) or (47 <= LA9_8 <= 63) or (65 <= LA9_8 <= 65535)):
                    s = 8

                else:
                    s = 29

                if s >= 0:
                    return s
            elif s == 1: 
                LA9_39 = input.LA(1)

                 
                index9_39 = input.index()
                input.rewind()
                s = -1
                if ((97 <= LA9_39 <= 122)):
                    s = 20

                elif ((65 <= LA9_39 <= 90)):
                    s = 21

                elif ((48 <= LA9_39 <= 57)):
                    s = 22

                elif (LA9_39 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_39 == 45):
                    s = 23

                elif (LA9_39 == 95):
                    s = 25

                elif (LA9_39 == 32):
                    s = 19

                elif ((0 <= LA9_39 <= 8) or LA9_39 == 11 or (14 <= LA9_39 <= 31) or (33 <= LA9_39 <= 44) or LA9_39 == 47 or (58 <= LA9_39 <= 63) or (91 <= LA9_39 <= 94) or LA9_39 == 96 or (123 <= LA9_39 <= 65535)):
                    s = 8

                else:
                    s = 41

                 
                input.seek(index9_39)
                if s >= 0:
                    return s
            elif s == 2: 
                LA9_21 = input.LA(1)

                 
                index9_21 = input.index()
                input.rewind()
                s = -1
                if (LA9_21 == 32):
                    s = 19

                elif ((97 <= LA9_21 <= 122)):
                    s = 20

                elif ((65 <= LA9_21 <= 90)):
                    s = 21

                elif ((48 <= LA9_21 <= 57)):
                    s = 22

                elif (LA9_21 == 45):
                    s = 23

                elif (LA9_21 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_21 == 95):
                    s = 25

                elif ((0 <= LA9_21 <= 8) or LA9_21 == 11 or (14 <= LA9_21 <= 31) or (33 <= LA9_21 <= 44) or LA9_21 == 47 or (58 <= LA9_21 <= 63) or (91 <= LA9_21 <= 94) or LA9_21 == 96 or (123 <= LA9_21 <= 65535)):
                    s = 8

                else:
                    s = 35

                 
                input.seek(index9_21)
                if s >= 0:
                    return s
            elif s == 3: 
                LA9_22 = input.LA(1)

                 
                index9_22 = input.index()
                input.rewind()
                s = -1
                if ((97 <= LA9_22 <= 122)):
                    s = 20

                elif ((65 <= LA9_22 <= 90)):
                    s = 21

                elif ((48 <= LA9_22 <= 57)):
                    s = 22

                elif (LA9_22 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_22 == 45):
                    s = 23

                elif (LA9_22 == 95):
                    s = 25

                elif (LA9_22 == 32):
                    s = 19

                elif ((0 <= LA9_22 <= 8) or LA9_22 == 11 or (14 <= LA9_22 <= 31) or (33 <= LA9_22 <= 44) or LA9_22 == 47 or (58 <= LA9_22 <= 63) or (91 <= LA9_22 <= 94) or LA9_22 == 96 or (123 <= LA9_22 <= 65535)):
                    s = 8

                else:
                    s = 36

                 
                input.seek(index9_22)
                if s >= 0:
                    return s
            elif s == 4: 
                LA9_16 = input.LA(1)

                 
                index9_16 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 31

                 
                input.seek(index9_16)
                if s >= 0:
                    return s
            elif s == 5: 
                LA9_40 = input.LA(1)

                 
                index9_40 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_40)
                if s >= 0:
                    return s
            elif s == 6: 
                LA9_38 = input.LA(1)

                 
                index9_38 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_38)
                if s >= 0:
                    return s
            elif s == 7: 
                LA9_37 = input.LA(1)

                 
                index9_37 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_37)
                if s >= 0:
                    return s
            elif s == 8: 
                LA9_36 = input.LA(1)

                 
                index9_36 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_36)
                if s >= 0:
                    return s
            elif s == 9: 
                LA9_35 = input.LA(1)

                 
                index9_35 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_35)
                if s >= 0:
                    return s
            elif s == 10: 
                LA9_34 = input.LA(1)

                 
                index9_34 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_34)
                if s >= 0:
                    return s
            elif s == 11: 
                LA9_33 = input.LA(1)

                 
                index9_33 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_33)
                if s >= 0:
                    return s
            elif s == 12: 
                LA9_28 = input.LA(1)

                 
                index9_28 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_28)
                if s >= 0:
                    return s
            elif s == 13: 
                LA9_27 = input.LA(1)

                 
                index9_27 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_27)
                if s >= 0:
                    return s
            elif s == 14: 
                LA9_26 = input.LA(1)

                 
                index9_26 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_26)
                if s >= 0:
                    return s
            elif s == 15: 
                LA9_4 = input.LA(1)

                 
                index9_4 = input.index()
                input.rewind()
                s = -1
                if (LA9_4 == 32):
                    s = 19

                elif ((97 <= LA9_4 <= 122)):
                    s = 20

                elif ((65 <= LA9_4 <= 90)):
                    s = 21

                elif ((48 <= LA9_4 <= 57)):
                    s = 22

                elif (LA9_4 == 45):
                    s = 23

                elif (LA9_4 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_4 == 95):
                    s = 25

                elif ((0 <= LA9_4 <= 8) or LA9_4 == 11 or (14 <= LA9_4 <= 31) or (33 <= LA9_4 <= 44) or LA9_4 == 47 or (58 <= LA9_4 <= 63) or (91 <= LA9_4 <= 94) or LA9_4 == 96 or (123 <= LA9_4 <= 65535)):
                    s = 8

                else:
                    s = 26

                 
                input.seek(index9_4)
                if s >= 0:
                    return s
            elif s == 16: 
                LA9_18 = input.LA(1)

                 
                index9_18 = input.index()
                input.rewind()
                s = -1
                if (not (((self.tagMode)))):
                    s = 29

                elif ((self.tagMode)):
                    s = 24

                 
                input.seek(index9_18)
                if s >= 0:
                    return s
            elif s == 17: 
                LA9_20 = input.LA(1)

                 
                index9_20 = input.index()
                input.rewind()
                s = -1
                if ((97 <= LA9_20 <= 122)):
                    s = 20

                elif ((65 <= LA9_20 <= 90)):
                    s = 21

                elif ((48 <= LA9_20 <= 57)):
                    s = 22

                elif (LA9_20 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_20 == 45):
                    s = 23

                elif (LA9_20 == 95):
                    s = 25

                elif (LA9_20 == 32):
                    s = 19

                elif ((0 <= LA9_20 <= 8) or LA9_20 == 11 or (14 <= LA9_20 <= 31) or (33 <= LA9_20 <= 44) or LA9_20 == 47 or (58 <= LA9_20 <= 63) or (91 <= LA9_20 <= 94) or LA9_20 == 96 or (123 <= LA9_20 <= 65535)):
                    s = 8

                else:
                    s = 34

                 
                input.seek(index9_20)
                if s >= 0:
                    return s
            elif s == 18: 
                LA9_15 = input.LA(1)

                s = -1
                if ((0 <= LA9_15 <= 8) or LA9_15 == 11 or (14 <= LA9_15 <= 45) or (47 <= LA9_15 <= 63) or (65 <= LA9_15 <= 65535)):
                    s = 19

                else:
                    s = 30

                if s >= 0:
                    return s
            elif s == 19: 
                LA9_6 = input.LA(1)

                 
                index9_6 = input.index()
                input.rewind()
                s = -1
                if (LA9_6 == 32):
                    s = 19

                elif ((97 <= LA9_6 <= 122)):
                    s = 20

                elif ((65 <= LA9_6 <= 90)):
                    s = 21

                elif ((48 <= LA9_6 <= 57)):
                    s = 22

                elif (LA9_6 == 45):
                    s = 23

                elif (LA9_6 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_6 == 95):
                    s = 25

                elif ((0 <= LA9_6 <= 8) or LA9_6 == 11 or (14 <= LA9_6 <= 31) or (33 <= LA9_6 <= 44) or LA9_6 == 47 or (58 <= LA9_6 <= 63) or (91 <= LA9_6 <= 94) or LA9_6 == 96 or (123 <= LA9_6 <= 65535)):
                    s = 8

                else:
                    s = 27

                 
                input.seek(index9_6)
                if s >= 0:
                    return s
            elif s == 20: 
                LA9_2 = input.LA(1)

                s = -1
                if (LA9_2 == 32):
                    s = 15

                elif ((0 <= LA9_2 <= 8) or LA9_2 == 11 or (14 <= LA9_2 <= 31) or (33 <= LA9_2 <= 45) or (47 <= LA9_2 <= 63) or (65 <= LA9_2 <= 65535)):
                    s = 8

                else:
                    s = 16

                if s >= 0:
                    return s
            elif s == 21: 
                LA9_7 = input.LA(1)

                 
                index9_7 = input.index()
                input.rewind()
                s = -1
                if (LA9_7 == 32):
                    s = 19

                elif ((97 <= LA9_7 <= 122)):
                    s = 20

                elif ((65 <= LA9_7 <= 90)):
                    s = 21

                elif ((48 <= LA9_7 <= 57)):
                    s = 22

                elif (LA9_7 == 45):
                    s = 23

                elif (LA9_7 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_7 == 95):
                    s = 25

                elif ((0 <= LA9_7 <= 8) or LA9_7 == 11 or (14 <= LA9_7 <= 31) or (33 <= LA9_7 <= 44) or LA9_7 == 47 or (58 <= LA9_7 <= 63) or (91 <= LA9_7 <= 94) or LA9_7 == 96 or (123 <= LA9_7 <= 65535)):
                    s = 8

                else:
                    s = 28

                 
                input.seek(index9_7)
                if s >= 0:
                    return s
            elif s == 22: 
                LA9_25 = input.LA(1)

                 
                index9_25 = input.index()
                input.rewind()
                s = -1
                if (LA9_25 == 32):
                    s = 19

                elif ((97 <= LA9_25 <= 122)):
                    s = 20

                elif ((65 <= LA9_25 <= 90)):
                    s = 21

                elif ((48 <= LA9_25 <= 57)):
                    s = 22

                elif (LA9_25 == 45):
                    s = 23

                elif (LA9_25 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_25 == 95):
                    s = 25

                elif ((0 <= LA9_25 <= 8) or LA9_25 == 11 or (14 <= LA9_25 <= 31) or (33 <= LA9_25 <= 44) or LA9_25 == 47 or (58 <= LA9_25 <= 63) or (91 <= LA9_25 <= 94) or LA9_25 == 96 or (123 <= LA9_25 <= 65535)):
                    s = 8

                else:
                    s = 38

                 
                input.seek(index9_25)
                if s >= 0:
                    return s
            elif s == 23: 
                LA9_17 = input.LA(1)

                 
                index9_17 = input.index()
                input.rewind()
                s = -1
                if (LA9_17 == 110):
                    s = 32

                elif ((97 <= LA9_17 <= 109) or (111 <= LA9_17 <= 122)):
                    s = 20

                elif ((65 <= LA9_17 <= 90)):
                    s = 21

                elif ((48 <= LA9_17 <= 57)):
                    s = 22

                elif (LA9_17 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_17 == 45):
                    s = 23

                elif (LA9_17 == 95):
                    s = 25

                elif (LA9_17 == 32):
                    s = 19

                elif ((0 <= LA9_17 <= 8) or LA9_17 == 11 or (14 <= LA9_17 <= 31) or (33 <= LA9_17 <= 44) or LA9_17 == 47 or (58 <= LA9_17 <= 63) or (91 <= LA9_17 <= 94) or LA9_17 == 96 or (123 <= LA9_17 <= 65535)):
                    s = 8

                else:
                    s = 33

                 
                input.seek(index9_17)
                if s >= 0:
                    return s
            elif s == 24: 
                LA9_23 = input.LA(1)

                 
                index9_23 = input.index()
                input.rewind()
                s = -1
                if ((97 <= LA9_23 <= 122)):
                    s = 20

                elif ((65 <= LA9_23 <= 90)):
                    s = 21

                elif ((48 <= LA9_23 <= 57)):
                    s = 22

                elif (LA9_23 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_23 == 45):
                    s = 23

                elif (LA9_23 == 95):
                    s = 25

                elif (LA9_23 == 32):
                    s = 19

                elif ((0 <= LA9_23 <= 8) or LA9_23 == 11 or (14 <= LA9_23 <= 31) or (33 <= LA9_23 <= 44) or LA9_23 == 47 or (58 <= LA9_23 <= 63) or (91 <= LA9_23 <= 94) or LA9_23 == 96 or (123 <= LA9_23 <= 65535)):
                    s = 8

                else:
                    s = 37

                 
                input.seek(index9_23)
                if s >= 0:
                    return s
            elif s == 25: 
                LA9_32 = input.LA(1)

                 
                index9_32 = input.index()
                input.rewind()
                s = -1
                if (LA9_32 == 101):
                    s = 39

                elif ((97 <= LA9_32 <= 100) or (102 <= LA9_32 <= 122)):
                    s = 20

                elif ((65 <= LA9_32 <= 90)):
                    s = 21

                elif ((48 <= LA9_32 <= 57)):
                    s = 22

                elif (LA9_32 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_32 == 45):
                    s = 23

                elif (LA9_32 == 95):
                    s = 25

                elif (LA9_32 == 32):
                    s = 19

                elif ((0 <= LA9_32 <= 8) or LA9_32 == 11 or (14 <= LA9_32 <= 31) or (33 <= LA9_32 <= 44) or LA9_32 == 47 or (58 <= LA9_32 <= 63) or (91 <= LA9_32 <= 94) or LA9_32 == 96 or (123 <= LA9_32 <= 65535)):
                    s = 8

                else:
                    s = 40

                 
                input.seek(index9_32)
                if s >= 0:
                    return s
            elif s == 26: 
                LA9_3 = input.LA(1)

                 
                index9_3 = input.index()
                input.rewind()
                s = -1
                if (LA9_3 == 111):
                    s = 17

                elif (LA9_3 == 32):
                    s = 19

                elif ((97 <= LA9_3 <= 110) or (112 <= LA9_3 <= 122)):
                    s = 20

                elif ((65 <= LA9_3 <= 90)):
                    s = 21

                elif ((48 <= LA9_3 <= 57)):
                    s = 22

                elif (LA9_3 == 45):
                    s = 23

                elif (LA9_3 == 46) and ((self.tagMode)):
                    s = 24

                elif (LA9_3 == 95):
                    s = 25

                elif ((0 <= LA9_3 <= 8) or LA9_3 == 11 or (14 <= LA9_3 <= 31) or (33 <= LA9_3 <= 44) or LA9_3 == 47 or (58 <= LA9_3 <= 63) or (91 <= LA9_3 <= 94) or LA9_3 == 96 or (123 <= LA9_3 <= 65535)):
                    s = 8

                else:
                    s = 18

                 
                input.seek(index9_3)
                if s >= 0:
                    return s
            elif s == 27: 
                LA9_0 = input.LA(1)

                s = -1
                if (LA9_0 == 64):
                    s = 1

                elif (LA9_0 == 58):
                    s = 2

                elif (LA9_0 == 78):
                    s = 3

                elif ((97 <= LA9_0 <= 122)):
                    s = 4

                elif (LA9_0 == 46):
                    s = 5

                elif ((65 <= LA9_0 <= 77) or (79 <= LA9_0 <= 90)):
                    s = 6

                elif (LA9_0 == 95):
                    s = 7

                elif ((0 <= LA9_0 <= 8) or LA9_0 == 11 or (14 <= LA9_0 <= 31) or (33 <= LA9_0 <= 45) or (47 <= LA9_0 <= 57) or (59 <= LA9_0 <= 63) or (91 <= LA9_0 <= 94) or LA9_0 == 96 or (123 <= LA9_0 <= 65535)):
                    s = 8

                elif (LA9_0 == 10 or LA9_0 == 13):
                    s = 9

                elif (LA9_0 == 9 or LA9_0 == 12 or LA9_0 == 32):
                    s = 10

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 9, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(DocStyleLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
