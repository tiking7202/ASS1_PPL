# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u01c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\3\2\5\2\177\n\2\3\3\6\3\u0082")
        buf.write("\n\3\r\3\16\3\u0083\3\4\6\4\u0087\n\4\r\4\16\4\u0088\3")
        buf.write("\4\3\4\3\5\3\5\5\5\u008f\n\5\3\5\6\5\u0092\n\5\r\5\16")
        buf.write("\5\u0093\3\6\3\6\3\6\3\6\3\6\5\6\u009b\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7\u00a2\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\5\37\u0120\n\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\7\63\u0151\n\63\f\63\16\63\u0154")
        buf.write("\13\63\3\64\6\64\u0157\n\64\r\64\16\64\u0158\3\65\3\65")
        buf.write("\5\65\u015d\n\65\3\65\5\65\u0160\n\65\3\65\5\65\u0163")
        buf.write("\n\65\3\65\5\65\u0166\n\65\3\66\3\66\7\66\u016a\n\66\f")
        buf.write("\66\16\66\u016d\13\66\3\66\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("8\38\78\u0178\n8\f8\168\u017b\138\38\38\39\69\u0180\n")
        buf.write("9\r9\169\u0181\39\39\3:\3:\7:\u0188\n:\f:\16:\u018b\13")
        buf.write(":\3:\3:\3:\5:\u0190\n:\3:\3:\3;\3;\7;\u0196\n;\f;\16;")
        buf.write("\u0199\13;\3;\3;\3;\5;\u019e\n;\3;\5;\u01a1\n;\3;\3;\3")
        buf.write(";\7;\u01a6\n;\f;\16;\u01a9\13;\3;\3;\3;\3;\3;\7;\u01b0")
        buf.write("\n;\f;\16;\u01b3\13;\3;\3;\7;\u01b7\n;\f;\16;\u01ba\13")
        buf.write(";\3;\3;\5;\u01be\n;\3<\3<\3<\2\2=\3\3\5\2\7\2\t\2\13\2")
        buf.write("\r\2\17\4\21\5\23\6\25\7\27\b\31\t\33\n\35\13\37\f!\r")
        buf.write("#\16%\17\'\20)\21+\22-\23/\24\61\25\63\26\65\27\67\30")
        buf.write("9\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[*]")
        buf.write("+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8\3\2\21\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2))^^ddhhppt")
        buf.write("tvv\6\2\f\f\16\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\3\2\f")
        buf.write("\f\4\2\f\f\16\17\5\2\n\13\16\17\"\"\3\3\f\f\6\2\17\17")
        buf.write("$$))^^\3\2\17\17\7\2\f\f\17\17$$))^^\2\u01d9\2\3\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\3~\3\2\2\2\5\u0081\3\2\2\2\7")
        buf.write("\u0086\3\2\2\2\t\u008c\3\2\2\2\13\u009a\3\2\2\2\r\u00a1")
        buf.write("\3\2\2\2\17\u00a3\3\2\2\2\21\u00a8\3\2\2\2\23\u00ae\3")
        buf.write("\2\2\2\25\u00b5\3\2\2\2\27\u00ba\3\2\2\2\31\u00c1\3\2")
        buf.write("\2\2\33\u00c8\3\2\2\2\35\u00cc\3\2\2\2\37\u00d4\3\2\2")
        buf.write("\2!\u00d9\3\2\2\2#\u00dd\3\2\2\2%\u00e3\3\2\2\2\'\u00e6")
        buf.write("\3\2\2\2)\u00ec\3\2\2\2+\u00f5\3\2\2\2-\u00f8\3\2\2\2")
        buf.write("/\u00fd\3\2\2\2\61\u0102\3\2\2\2\63\u0108\3\2\2\2\65\u010c")
        buf.write("\3\2\2\2\67\u0110\3\2\2\29\u0113\3\2\2\2;\u0117\3\2\2")
        buf.write("\2=\u011f\3\2\2\2?\u0121\3\2\2\2A\u0123\3\2\2\2C\u0125")
        buf.write("\3\2\2\2E\u0127\3\2\2\2G\u0129\3\2\2\2I\u012b\3\2\2\2")
        buf.write("K\u012d\3\2\2\2M\u0130\3\2\2\2O\u0133\3\2\2\2Q\u0136\3")
        buf.write("\2\2\2S\u0138\3\2\2\2U\u013b\3\2\2\2W\u013d\3\2\2\2Y\u0140")
        buf.write("\3\2\2\2[\u0144\3\2\2\2]\u0146\3\2\2\2_\u0148\3\2\2\2")
        buf.write("a\u014a\3\2\2\2c\u014c\3\2\2\2e\u014e\3\2\2\2g\u0156\3")
        buf.write("\2\2\2i\u0165\3\2\2\2k\u0167\3\2\2\2m\u0171\3\2\2\2o\u0173")
        buf.write("\3\2\2\2q\u017f\3\2\2\2s\u0185\3\2\2\2u\u01bd\3\2\2\2")
        buf.write("w\u01bf\3\2\2\2yz\5g\64\2z{\5c\62\2{|\5\3\2\2|\177\3\2")
        buf.write("\2\2}\177\5g\64\2~y\3\2\2\2~}\3\2\2\2\177\4\3\2\2\2\u0080")
        buf.write("\u0082\t\2\2\2\u0081\u0080\3\2\2\2\u0082\u0083\3\2\2\2")
        buf.write("\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\6\3\2\2")
        buf.write("\2\u0085\u0087\t\2\2\2\u0086\u0085\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u008b\7\60\2\2\u008b\b\3\2\2\2\u008c")
        buf.write("\u008e\t\3\2\2\u008d\u008f\t\4\2\2\u008e\u008d\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u0092\t")
        buf.write("\2\2\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\n\3\2\2\2\u0095\u009b")
        buf.write("\n\5\2\2\u0096\u0097\7^\2\2\u0097\u009b\t\6\2\2\u0098")
        buf.write("\u0099\7)\2\2\u0099\u009b\7$\2\2\u009a\u0095\3\2\2\2\u009a")
        buf.write("\u0096\3\2\2\2\u009a\u0098\3\2\2\2\u009b\f\3\2\2\2\u009c")
        buf.write("\u00a2\n\7\2\2\u009d\u009e\7^\2\2\u009e\u00a2\t\6\2\2")
        buf.write("\u009f\u00a0\7)\2\2\u00a0\u00a2\7$\2\2\u00a1\u009c\3\2")
        buf.write("\2\2\u00a1\u009d\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\16")
        buf.write("\3\2\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7g\2\2\u00a7\20\3\2\2\2\u00a8\u00a9")
        buf.write("\7h\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac")
        buf.write("\7u\2\2\u00ac\u00ad\7g\2\2\u00ad\22\3\2\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7o\2\2\u00b1\u00b2")
        buf.write("\7d\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7t\2\2\u00b4\24")
        buf.write("\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7n\2\2\u00b9\26\3\2\2\2\u00ba\u00bb")
        buf.write("\7u\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7i\2\2\u00c0\30")
        buf.write("\3\2\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7v\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\32\3\2\2\2\u00c8\u00c9\7x\2\2\u00c9\u00ca")
        buf.write("\7c\2\2\u00ca\u00cb\7t\2\2\u00cb\34\3\2\2\2\u00cc\u00cd")
        buf.write("\7f\2\2\u00cd\u00ce\7{\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7c\2\2\u00d0\u00d1\7o\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7e\2\2\u00d3\36\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6")
        buf.write("\7w\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7e\2\2\u00d8 \3")
        buf.write("\2\2\2\u00d9\u00da\7h\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7t\2\2\u00dc\"\3\2\2\2\u00dd\u00de\7w\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2")
        buf.write("\7n\2\2\u00e2$\3\2\2\2\u00e3\u00e4\7d\2\2\u00e4\u00e5")
        buf.write("\7{\2\2\u00e5&\3\2\2\2\u00e6\u00e7\7d\2\2\u00e7\u00e8")
        buf.write("\7t\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb")
        buf.write("\7m\2\2\u00eb(\3\2\2\2\u00ec\u00ed\7e\2\2\u00ed\u00ee")
        buf.write("\7q\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1")
        buf.write("\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7w\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4*\3\2\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7,\3\2\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa")
        buf.write("\7n\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc\7g\2\2\u00fc.\3")
        buf.write("\2\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7h\2\2\u0101\60\3\2\2\2\u0102\u0103")
        buf.write("\7d\2\2\u0103\u0104\7g\2\2\u0104\u0105\7i\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7p\2\2\u0107\62\3\2\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010a\7p\2\2\u010a\u010b\7f\2\2\u010b\64")
        buf.write("\3\2\2\2\u010c\u010d\7c\2\2\u010d\u010e\7p\2\2\u010e\u010f")
        buf.write("\7f\2\2\u010f\66\3\2\2\2\u0110\u0111\7q\2\2\u0111\u0112")
        buf.write("\7t\2\2\u01128\3\2\2\2\u0113\u0114\7p\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7v\2\2\u0116:\3\2\2\2\u0117\u0118")
        buf.write("\7y\2\2\u0118\u0119\7j\2\2\u0119\u011a\7k\2\2\u011a\u011b")
        buf.write("\7n\2\2\u011b\u011c\7g\2\2\u011c<\3\2\2\2\u011d\u0120")
        buf.write("\5\17\b\2\u011e\u0120\5\21\t\2\u011f\u011d\3\2\2\2\u011f")
        buf.write("\u011e\3\2\2\2\u0120>\3\2\2\2\u0121\u0122\7-\2\2\u0122")
        buf.write("@\3\2\2\2\u0123\u0124\7/\2\2\u0124B\3\2\2\2\u0125\u0126")
        buf.write("\7,\2\2\u0126D\3\2\2\2\u0127\u0128\7\61\2\2\u0128F\3\2")
        buf.write("\2\2\u0129\u012a\7\'\2\2\u012aH\3\2\2\2\u012b\u012c\7")
        buf.write("?\2\2\u012cJ\3\2\2\2\u012d\u012e\7>\2\2\u012e\u012f\7")
        buf.write("/\2\2\u012fL\3\2\2\2\u0130\u0131\7?\2\2\u0131\u0132\7")
        buf.write("?\2\2\u0132N\3\2\2\2\u0133\u0134\7#\2\2\u0134\u0135\7")
        buf.write("?\2\2\u0135P\3\2\2\2\u0136\u0137\7>\2\2\u0137R\3\2\2\2")
        buf.write("\u0138\u0139\7>\2\2\u0139\u013a\7?\2\2\u013aT\3\2\2\2")
        buf.write("\u013b\u013c\7@\2\2\u013cV\3\2\2\2\u013d\u013e\7@\2\2")
        buf.write("\u013e\u013f\7?\2\2\u013fX\3\2\2\2\u0140\u0141\7\60\2")
        buf.write("\2\u0141\u0142\7\60\2\2\u0142\u0143\7\60\2\2\u0143Z\3")
        buf.write("\2\2\2\u0144\u0145\7*\2\2\u0145\\\3\2\2\2\u0146\u0147")
        buf.write("\7+\2\2\u0147^\3\2\2\2\u0148\u0149\7]\2\2\u0149`\3\2\2")
        buf.write("\2\u014a\u014b\7_\2\2\u014bb\3\2\2\2\u014c\u014d\7.\2")
        buf.write("\2\u014dd\3\2\2\2\u014e\u0152\t\b\2\2\u014f\u0151\t\t")
        buf.write("\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150")
        buf.write("\3\2\2\2\u0152\u0153\3\2\2\2\u0153f\3\2\2\2\u0154\u0152")
        buf.write("\3\2\2\2\u0155\u0157\t\2\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159h\3\2\2\2\u015a\u015c\5\7\4\2\u015b\u015d\5\5\3")
        buf.write("\2\u015c\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u0166")
        buf.write("\3\2\2\2\u015e\u0160\5\7\4\2\u015f\u015e\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u0163\5\5\3\2")
        buf.write("\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3")
        buf.write("\2\2\2\u0164\u0166\5\t\5\2\u0165\u015a\3\2\2\2\u0165\u015f")
        buf.write("\3\2\2\2\u0166j\3\2\2\2\u0167\u016b\7$\2\2\u0168\u016a")
        buf.write("\5\r\7\2\u0169\u0168\3\2\2\2\u016a\u016d\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016e\u016f\7$\2\2\u016f\u0170\b")
        buf.write("\66\2\2\u0170l\3\2\2\2\u0171\u0172\t\n\2\2\u0172n\3\2")
        buf.write("\2\2\u0173\u0174\7%\2\2\u0174\u0175\7%\2\2\u0175\u0179")
        buf.write("\3\2\2\2\u0176\u0178\n\13\2\2\u0177\u0176\3\2\2\2\u0178")
        buf.write("\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u017c\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017d\b")
        buf.write("8\3\2\u017dp\3\2\2\2\u017e\u0180\t\f\2\2\u017f\u017e\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\b9\3\2\u0184")
        buf.write("r\3\2\2\2\u0185\u0189\7$\2\2\u0186\u0188\5\r\7\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a\u018f\3\2\2\2\u018b\u0189\3")
        buf.write("\2\2\2\u018c\u018d\7\17\2\2\u018d\u0190\7\f\2\2\u018e")
        buf.write("\u0190\t\r\2\2\u018f\u018c\3\2\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191\u0192\b:\4\2\u0192t\3\2\2\2")
        buf.write("\u0193\u0197\7$\2\2\u0194\u0196\5\13\6\2\u0195\u0194\3")
        buf.write("\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198\u019d\3\2\2\2\u0199\u0197\3\2\2\2\u019a")
        buf.write("\u019b\7^\2\2\u019b\u019e\n\16\2\2\u019c\u019e\t\17\2")
        buf.write("\2\u019d\u019a\3\2\2\2\u019d\u019c\3\2\2\2\u019e\u01a0")
        buf.write("\3\2\2\2\u019f\u01a1\7$\2\2\u01a0\u019f\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01be\b;\5\2")
        buf.write("\u01a3\u01a7\7$\2\2\u01a4\u01a6\5\13\6\2\u01a5\u01a4\3")
        buf.write("\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa")
        buf.write("\u01ab\7^\2\2\u01ab\u01ac\7$\2\2\u01ac\u01be\b;\6\2\u01ad")
        buf.write("\u01b1\7$\2\2\u01ae\u01b0\5\13\6\2\u01af\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3")
        buf.write("\2\2\2\u01b2\u01b8\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5")
        buf.write("\7)\2\2\u01b5\u01b7\n\20\2\2\u01b6\u01b4\3\2\2\2\u01b7")
        buf.write("\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2")
        buf.write("\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7")
        buf.write("$\2\2\u01bc\u01be\b;\7\2\u01bd\u0193\3\2\2\2\u01bd\u01a3")
        buf.write("\3\2\2\2\u01bd\u01ad\3\2\2\2\u01bev\3\2\2\2\u01bf\u01c0")
        buf.write("\13\2\2\2\u01c0\u01c1\b<\b\2\u01c1x\3\2\2\2\35\2~\u0083")
        buf.write("\u0088\u008e\u0093\u009a\u00a1\u011f\u0152\u0158\u015c")
        buf.write("\u015f\u0162\u0165\u016b\u0179\u0181\u0189\u018f\u0197")
        buf.write("\u019d\u01a0\u01a7\u01b1\u01b8\u01bd\t\3\66\2\b\2\2\3")
        buf.write(":\3\3;\4\3;\5\3;\6\3<\7")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER_list = 1
    TRUE = 2
    FALSE = 3
    NUMBER = 4
    BOOL = 5
    STRING = 6
    RETURN = 7
    VAR = 8
    DYNAMIC = 9
    FUNC = 10
    FOR = 11
    UNTIL = 12
    BY = 13
    BREAK = 14
    CONTINUE = 15
    IF = 16
    ELSE = 17
    ELIF = 18
    BEGIN = 19
    END = 20
    AND = 21
    OR = 22
    NOT = 23
    WHILE = 24
    BOOLEAN = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    ASSIGN = 31
    ASSIGNINIT = 32
    EQUAL = 33
    NOT_EQUAL = 34
    LESS = 35
    LESS_EQUAL = 36
    GREAT = 37
    GREAT_EQUAL = 38
    CONCAT = 39
    LB = 40
    RB = 41
    LP = 42
    RP = 43
    COMMA = 44
    ID = 45
    INT = 46
    REAL = 47
    STRING_LIT = 48
    NEWLINE = 49
    COMMENTS = 50
    WS = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESCAPE = 53
    ERROR_CHAR = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'and'", "'or'", "'not'", "'while'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'='", "'<-'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'...'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER_list", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
            "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "AND", "OR", 
            "NOT", "WHILE", "BOOLEAN", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "ASSIGN", "ASSIGNINIT", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
            "GREAT", "GREAT_EQUAL", "CONCAT", "LB", "RB", "LP", "RP", "COMMA", 
            "ID", "INT", "REAL", "STRING_LIT", "NEWLINE", "COMMENTS", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "NUMBER_list", "INPART", "DEPART", "EXPART", "ILLSTRING", 
                  "STRINGCHAR", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "AND", "OR", "NOT", "WHILE", "BOOLEAN", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "ASSIGN", "ASSIGNINIT", "EQUAL", 
                  "NOT_EQUAL", "LESS", "LESS_EQUAL", "GREAT", "GREAT_EQUAL", 
                  "CONCAT", "LB", "RB", "LP", "RP", "COMMA", "ID", "INT", 
                  "REAL", "STRING_LIT", "NEWLINE", "COMMENTS", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.STRING_LIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	if self.text[-1] == '\n' and self.text[-2] == '\r':
            		raise UncloseString(self.text[1:-2])
            	elif self.text[-1] == '\n':
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    if self.text[-1] == '"':
                        raise IllegalEscape(self.text[1:-1])

                    raise IllegalEscape(self.text[1:])
                
     

        if actionIndex == 3:

                        raise IllegalEscape(self.text[1:])
                
     

        if actionIndex == 4:

                    raise IllegalEscape(self.text[1:-1])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


