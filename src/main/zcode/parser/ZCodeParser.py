# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u0175\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\3\2\3\2\7\2R\n\2\f\2\16\2U\13\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\5\3^\n\3\3\4\3\4\3\4\3\4\5\4d\n\4")
        buf.write("\3\5\3\5\3\5\5\5i\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\5\7t\n\7\3\7\5\7w\n\7\3\7\3\7\3\7\3\7\5\7}\n\7\3")
        buf.write("\7\5\7\u0080\n\7\3\7\3\7\5\7\u0084\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u008c\n\b\5\b\u008e\n\b\3\t\3\t\3\t\3\t\5")
        buf.write("\t\u0094\n\t\3\t\3\t\5\t\u0098\n\t\3\t\3\t\5\t\u009c\n")
        buf.write("\t\3\t\3\t\5\t\u00a0\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a7")
        buf.write("\n\n\3\n\3\n\5\n\u00ab\n\n\3\13\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00b2\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00b9\n\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00c0\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00c7\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00ce\n")
        buf.write("\17\3\20\3\20\3\20\5\20\u00d3\n\20\3\21\3\21\3\21\5\21")
        buf.write("\u00d8\n\21\3\22\3\22\5\22\u00dc\n\22\3\22\3\22\5\22\u00e0")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e9\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\5\24\u00f0\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u00f8\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0107\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u0112\n\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\5\34\u011f\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u0126\n\35\3\35\3\35\5\35\u012a\n\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0131\n\36\3\36\3\36\5\36\u0135")
        buf.write("\n\36\3\36\3\36\5\36\u0139\n\36\3\36\5\36\u013c\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0145\n\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\5\"\u0151\n\"\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0160\n$\3%\3%\3")
        buf.write("%\5%\u0165\n%\3%\3%\3%\3&\3&\3&\3&\5&\u016e\n&\3\'\6\'")
        buf.write("\u0171\n\'\r\'\16\'\u0172\3\'\2\2(\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL\2\7")
        buf.write("\3\2\6\b\4\2!!#(\3\2\27\30\3\2\34\35\3\2\36 \2\u018a\2")
        buf.write("S\3\2\2\2\4]\3\2\2\2\6c\3\2\2\2\bh\3\2\2\2\nj\3\2\2\2")
        buf.write("\f\u0083\3\2\2\2\16\u008d\3\2\2\2\20\u008f\3\2\2\2\22")
        buf.write("\u00a1\3\2\2\2\24\u00b1\3\2\2\2\26\u00b8\3\2\2\2\30\u00bf")
        buf.write("\3\2\2\2\32\u00c6\3\2\2\2\34\u00cd\3\2\2\2\36\u00d2\3")
        buf.write("\2\2\2 \u00d7\3\2\2\2\"\u00df\3\2\2\2$\u00e8\3\2\2\2&")
        buf.write("\u00ef\3\2\2\2(\u00f7\3\2\2\2*\u00f9\3\2\2\2,\u00fd\3")
        buf.write("\2\2\2.\u0106\3\2\2\2\60\u0111\3\2\2\2\62\u0113\3\2\2")
        buf.write("\2\64\u0116\3\2\2\2\66\u011e\3\2\2\28\u0120\3\2\2\2:\u013b")
        buf.write("\3\2\2\2<\u013d\3\2\2\2>\u0148\3\2\2\2@\u014b\3\2\2\2")
        buf.write("B\u014e\3\2\2\2D\u0154\3\2\2\2F\u015f\3\2\2\2H\u0161\3")
        buf.write("\2\2\2J\u016d\3\2\2\2L\u0170\3\2\2\2NO\7\64\2\2OR\7\63")
        buf.write("\2\2PR\7\63\2\2QN\3\2\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2")
        buf.write("\2ST\3\2\2\2TV\3\2\2\2US\3\2\2\2VW\5\4\3\2WX\7\2\2\3X")
        buf.write("\3\3\2\2\2YZ\5\6\4\2Z[\5\4\3\2[^\3\2\2\2\\^\5\6\4\2]Y")
        buf.write("\3\2\2\2]\\\3\2\2\2^\5\3\2\2\2_d\5\20\t\2`a\5\b\5\2ab")
        buf.write("\5L\'\2bd\3\2\2\2c_\3\2\2\2c`\3\2\2\2d\7\3\2\2\2ei\5\n")
        buf.write("\6\2fi\5\f\7\2gi\5\16\b\2he\3\2\2\2hf\3\2\2\2hg\3\2\2")
        buf.write("\2i\t\3\2\2\2jk\7\n\2\2kl\7/\2\2lm\7\"\2\2mn\5\24\13\2")
        buf.write("n\13\3\2\2\2op\t\2\2\2pv\7/\2\2qs\7,\2\2rt\7\3\2\2sr\3")
        buf.write("\2\2\2st\3\2\2\2tu\3\2\2\2uw\7-\2\2vq\3\2\2\2vw\3\2\2")
        buf.write("\2w\u0084\3\2\2\2xy\t\2\2\2y\177\7/\2\2z|\7,\2\2{}\7\3")
        buf.write("\2\2|{\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\u0080\7-\2\2\177z")
        buf.write("\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082")
        buf.write("\7\"\2\2\u0082\u0084\5\24\13\2\u0083o\3\2\2\2\u0083x\3")
        buf.write("\2\2\2\u0084\r\3\2\2\2\u0085\u0086\7\13\2\2\u0086\u008e")
        buf.write("\7/\2\2\u0087\u0088\7\13\2\2\u0088\u0089\7/\2\2\u0089")
        buf.write("\u008b\7\"\2\2\u008a\u008c\5\24\13\2\u008b\u008a\3\2\2")
        buf.write("\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u0085")
        buf.write("\3\2\2\2\u008d\u0087\3\2\2\2\u008e\17\3\2\2\2\u008f\u0090")
        buf.write("\7\f\2\2\u0090\u0091\7/\2\2\u0091\u0093\7*\2\2\u0092\u0094")
        buf.write("\5\22\n\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u009f\7+\2\2\u0096\u0098\5L\'\2\u0097")
        buf.write("\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u00a0\5B\"\2\u009a\u009c\5L\'\2\u009b\u009a\3\2")
        buf.write("\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u00a0")
        buf.write("\5H%\2\u009e\u00a0\5L\'\2\u009f\u0097\3\2\2\2\u009f\u009b")
        buf.write("\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\21\3\2\2\2\u00a1\u00a2")
        buf.write("\t\2\2\2\u00a2\u00a6\7/\2\2\u00a3\u00a4\7,\2\2\u00a4\u00a5")
        buf.write("\7\3\2\2\u00a5\u00a7\7-\2\2\u00a6\u00a3\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a9\7.\2\2")
        buf.write("\u00a9\u00ab\5\22\n\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\23\3\2\2\2\u00ac\u00ad\5\26\f\2\u00ad\u00ae")
        buf.write("\7)\2\2\u00ae\u00af\5\26\f\2\u00af\u00b2\3\2\2\2\u00b0")
        buf.write("\u00b2\5\26\f\2\u00b1\u00ac\3\2\2\2\u00b1\u00b0\3\2\2")
        buf.write("\2\u00b2\25\3\2\2\2\u00b3\u00b4\5\30\r\2\u00b4\u00b5\t")
        buf.write("\3\2\2\u00b5\u00b6\5\30\r\2\u00b6\u00b9\3\2\2\2\u00b7")
        buf.write("\u00b9\5\30\r\2\u00b8\u00b3\3\2\2\2\u00b8\u00b7\3\2\2")
        buf.write("\2\u00b9\27\3\2\2\2\u00ba\u00bb\5\32\16\2\u00bb\u00bc")
        buf.write("\t\4\2\2\u00bc\u00bd\5\30\r\2\u00bd\u00c0\3\2\2\2\u00be")
        buf.write("\u00c0\5\32\16\2\u00bf\u00ba\3\2\2\2\u00bf\u00be\3\2\2")
        buf.write("\2\u00c0\31\3\2\2\2\u00c1\u00c2\5\34\17\2\u00c2\u00c3")
        buf.write("\t\5\2\2\u00c3\u00c4\5\32\16\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c7\5\34\17\2\u00c6\u00c1\3\2\2\2\u00c6\u00c5\3\2\2")
        buf.write("\2\u00c7\33\3\2\2\2\u00c8\u00c9\5\36\20\2\u00c9\u00ca")
        buf.write("\t\6\2\2\u00ca\u00cb\5\34\17\2\u00cb\u00ce\3\2\2\2\u00cc")
        buf.write("\u00ce\5\36\20\2\u00cd\u00c8\3\2\2\2\u00cd\u00cc\3\2\2")
        buf.write("\2\u00ce\35\3\2\2\2\u00cf\u00d0\7\31\2\2\u00d0\u00d3\5")
        buf.write("\36\20\2\u00d1\u00d3\5 \21\2\u00d2\u00cf\3\2\2\2\u00d2")
        buf.write("\u00d1\3\2\2\2\u00d3\37\3\2\2\2\u00d4\u00d5\t\5\2\2\u00d5")
        buf.write("\u00d8\5 \21\2\u00d6\u00d8\5\"\22\2\u00d7\u00d4\3\2\2")
        buf.write("\2\u00d7\u00d6\3\2\2\2\u00d8!\3\2\2\2\u00d9\u00dc\7/\2")
        buf.write("\2\u00da\u00dc\5F$\2\u00db\u00d9\3\2\2\2\u00db\u00da\3")
        buf.write("\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e0\5,\27\2\u00de\u00e0")
        buf.write("\5$\23\2\u00df\u00db\3\2\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write("#\3\2\2\2\u00e1\u00e9\5(\25\2\u00e2\u00e3\7*\2\2\u00e3")
        buf.write("\u00e4\5\24\13\2\u00e4\u00e5\7+\2\2\u00e5\u00e9\3\2\2")
        buf.write("\2\u00e6\u00e9\7/\2\2\u00e7\u00e9\5F$\2\u00e8\u00e1\3")
        buf.write("\2\2\2\u00e8\u00e2\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7")
        buf.write("\3\2\2\2\u00e9%\3\2\2\2\u00ea\u00eb\5\24\13\2\u00eb\u00ec")
        buf.write("\7.\2\2\u00ec\u00ed\5&\24\2\u00ed\u00f0\3\2\2\2\u00ee")
        buf.write("\u00f0\5\24\13\2\u00ef\u00ea\3\2\2\2\u00ef\u00ee\3\2\2")
        buf.write("\2\u00f0\'\3\2\2\2\u00f1\u00f8\7\60\2\2\u00f2\u00f8\7")
        buf.write("\61\2\2\u00f3\u00f8\7\62\2\2\u00f4\u00f8\7\4\2\2\u00f5")
        buf.write("\u00f8\7\5\2\2\u00f6\u00f8\5*\26\2\u00f7\u00f1\3\2\2\2")
        buf.write("\u00f7\u00f2\3\2\2\2\u00f7\u00f3\3\2\2\2\u00f7\u00f4\3")
        buf.write("\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8)")
        buf.write("\3\2\2\2\u00f9\u00fa\7,\2\2\u00fa\u00fb\5&\24\2\u00fb")
        buf.write("\u00fc\7-\2\2\u00fc+\3\2\2\2\u00fd\u00fe\7,\2\2\u00fe")
        buf.write("\u00ff\5.\30\2\u00ff\u0100\7-\2\2\u0100-\3\2\2\2\u0101")
        buf.write("\u0102\5\24\13\2\u0102\u0103\7.\2\2\u0103\u0104\5.\30")
        buf.write("\2\u0104\u0107\3\2\2\2\u0105\u0107\5\24\13\2\u0106\u0101")
        buf.write("\3\2\2\2\u0106\u0105\3\2\2\2\u0107/\3\2\2\2\u0108\u0112")
        buf.write("\5\62\32\2\u0109\u0112\5\64\33\2\u010a\u0112\58\35\2\u010b")
        buf.write("\u0112\5<\37\2\u010c\u0112\5> \2\u010d\u0112\5@!\2\u010e")
        buf.write("\u0112\5B\"\2\u010f\u0112\5D#\2\u0110\u0112\5H%\2\u0111")
        buf.write("\u0108\3\2\2\2\u0111\u0109\3\2\2\2\u0111\u010a\3\2\2\2")
        buf.write("\u0111\u010b\3\2\2\2\u0111\u010c\3\2\2\2\u0111\u010d\3")
        buf.write("\2\2\2\u0111\u010e\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0110")
        buf.write("\3\2\2\2\u0112\61\3\2\2\2\u0113\u0114\5\b\5\2\u0114\u0115")
        buf.write("\5L\'\2\u0115\63\3\2\2\2\u0116\u0117\5\66\34\2\u0117\u0118")
        buf.write("\7\"\2\2\u0118\u0119\5\24\13\2\u0119\u011a\5L\'\2\u011a")
        buf.write("\65\3\2\2\2\u011b\u011c\7/\2\2\u011c\u011f\5,\27\2\u011d")
        buf.write("\u011f\7/\2\2\u011e\u011b\3\2\2\2\u011e\u011d\3\2\2\2")
        buf.write("\u011f\67\3\2\2\2\u0120\u0121\7\22\2\2\u0121\u0122\7*")
        buf.write("\2\2\u0122\u0123\5\24\13\2\u0123\u0125\7-\2\2\u0124\u0126")
        buf.write("\5L\'\2\u0125\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0129\5J&\2\u0128\u012a\5:\36\2\u0129")
        buf.write("\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a9\3\2\2\2\u012b")
        buf.write("\u012c\7\24\2\2\u012c\u012d\7*\2\2\u012d\u012e\5\24\13")
        buf.write("\2\u012e\u0130\7+\2\2\u012f\u0131\5L\'\2\u0130\u012f\3")
        buf.write("\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134")
        buf.write("\5J&\2\u0133\u0135\5:\36\2\u0134\u0133\3\2\2\2\u0134\u0135")
        buf.write("\3\2\2\2\u0135\u013c\3\2\2\2\u0136\u0138\7\23\2\2\u0137")
        buf.write("\u0139\5L\'\2\u0138\u0137\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u013c\5J&\2\u013b\u012b\3\2")
        buf.write("\2\2\u013b\u0136\3\2\2\2\u013c;\3\2\2\2\u013d\u013e\7")
        buf.write("\r\2\2\u013e\u013f\7/\2\2\u013f\u0140\7\16\2\2\u0140\u0141")
        buf.write("\5\24\13\2\u0141\u0142\7\17\2\2\u0142\u0144\5\24\13\2")
        buf.write("\u0143\u0145\5L\'\2\u0144\u0143\3\2\2\2\u0144\u0145\3")
        buf.write("\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\5J&\2\u0147=\3")
        buf.write("\2\2\2\u0148\u0149\7\20\2\2\u0149\u014a\5L\'\2\u014a?")
        buf.write("\3\2\2\2\u014b\u014c\7\21\2\2\u014c\u014d\5L\'\2\u014d")
        buf.write("A\3\2\2\2\u014e\u0150\7\t\2\2\u014f\u0151\5\24\13\2\u0150")
        buf.write("\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0153\5L\'\2\u0153C\3\2\2\2\u0154\u0155\5F$\2\u0155")
        buf.write("\u0156\5L\'\2\u0156E\3\2\2\2\u0157\u0158\7/\2\2\u0158")
        buf.write("\u0159\7*\2\2\u0159\u015a\5.\30\2\u015a\u015b\7+\2\2\u015b")
        buf.write("\u0160\3\2\2\2\u015c\u015d\7/\2\2\u015d\u015e\7*\2\2\u015e")
        buf.write("\u0160\7+\2\2\u015f\u0157\3\2\2\2\u015f\u015c\3\2\2\2")
        buf.write("\u0160G\3\2\2\2\u0161\u0162\7\25\2\2\u0162\u0164\5L\'")
        buf.write("\2\u0163\u0165\5J&\2\u0164\u0163\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\7\26\2\2\u0167")
        buf.write("\u0168\5L\'\2\u0168I\3\2\2\2\u0169\u016a\5\60\31\2\u016a")
        buf.write("\u016b\5J&\2\u016b\u016e\3\2\2\2\u016c\u016e\5\60\31\2")
        buf.write("\u016d\u0169\3\2\2\2\u016d\u016c\3\2\2\2\u016eK\3\2\2")
        buf.write("\2\u016f\u0171\7\63\2\2\u0170\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("M\3\2\2\2/QS]chsv|\177\u0083\u008b\u008d\u0093\u0097\u009b")
        buf.write("\u009f\u00a6\u00aa\u00b1\u00b8\u00bf\u00c6\u00cd\u00d2")
        buf.write("\u00d7\u00db\u00df\u00e8\u00ef\u00f7\u0106\u0111\u011e")
        buf.write("\u0125\u0129\u0130\u0134\u0138\u013b\u0144\u0150\u015f")
        buf.write("\u0164\u016d\u0172")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'and'", 
                     "'or'", "'not'", "'while'", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'='", "'<-'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'...'", "'('", "')'", 
                     "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "NUMBER_list", "TRUE", "FALSE", "NUMBER", 
                      "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "AND", "OR", "NOT", "WHILE", 
                      "BOOLEAN", "ADD", "SUB", "MUL", "DIV", "MOD", "ASSIGN", 
                      "ASSIGNINIT", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                      "GREAT", "GREAT_EQUAL", "CONCAT", "LB", "RB", "LP", 
                      "RP", "COMMA", "ID", "INT", "REAL", "STRING_LIT", 
                      "NEWLINE", "COMMENTS", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_variables = 3
    RULE_implicit_var = 4
    RULE_keyword_var = 5
    RULE_implicit_dynamic = 6
    RULE_function = 7
    RULE_prameters_list = 8
    RULE_expression = 9
    RULE_exp1 = 10
    RULE_exp2 = 11
    RULE_exp3 = 12
    RULE_exp4 = 13
    RULE_exp5 = 14
    RULE_exp6 = 15
    RULE_exp7 = 16
    RULE_exp8 = 17
    RULE_literals_list = 18
    RULE_literals = 19
    RULE_arr_literals = 20
    RULE_element_expr = 21
    RULE_indx_operator = 22
    RULE_statement = 23
    RULE_decl_stmt = 24
    RULE_assignment_statement = 25
    RULE_lhs = 26
    RULE_if_statement = 27
    RULE_elseif_statement = 28
    RULE_for_statement = 29
    RULE_break_statement = 30
    RULE_continue_statement = 31
    RULE_return_statement = 32
    RULE_call_statement = 33
    RULE_func_call = 34
    RULE_block_stmt = 35
    RULE_stmt = 36
    RULE_ignore = 37

    ruleNames =  [ "program", "decl_list", "decl", "variables", "implicit_var", 
                   "keyword_var", "implicit_dynamic", "function", "prameters_list", 
                   "expression", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "literals_list", "literals", 
                   "arr_literals", "element_expr", "indx_operator", "statement", 
                   "decl_stmt", "assignment_statement", "lhs", "if_statement", 
                   "elseif_statement", "for_statement", "break_statement", 
                   "continue_statement", "return_statement", "call_statement", 
                   "func_call", "block_stmt", "stmt", "ignore" ]

    EOF = Token.EOF
    NUMBER_list=1
    TRUE=2
    FALSE=3
    NUMBER=4
    BOOL=5
    STRING=6
    RETURN=7
    VAR=8
    DYNAMIC=9
    FUNC=10
    FOR=11
    UNTIL=12
    BY=13
    BREAK=14
    CONTINUE=15
    IF=16
    ELSE=17
    ELIF=18
    BEGIN=19
    END=20
    AND=21
    OR=22
    NOT=23
    WHILE=24
    BOOLEAN=25
    ADD=26
    SUB=27
    MUL=28
    DIV=29
    MOD=30
    ASSIGN=31
    ASSIGNINIT=32
    EQUAL=33
    NOT_EQUAL=34
    LESS=35
    LESS_EQUAL=36
    GREAT=37
    GREAT_EQUAL=38
    CONCAT=39
    LB=40
    RB=41
    LP=42
    RP=43
    COMMA=44
    ID=45
    INT=46
    REAL=47
    STRING_LIT=48
    NEWLINE=49
    COMMENTS=50
    WS=51
    UNCLOSE_STRING=52
    ILLEGAL_ESCAPE=53
    ERROR_CHAR=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def COMMENTS(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMENTS)
            else:
                return self.getToken(ZCodeParser.COMMENTS, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE or _la==ZCodeParser.COMMENTS:
                self.state = 79
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.COMMENTS]:
                    self.state = 76
                    self.match(ZCodeParser.COMMENTS)
                    self.state = 77
                    self.match(ZCodeParser.NEWLINE)
                    pass
                elif token in [ZCodeParser.NEWLINE]:
                    self.state = 78
                    self.match(ZCodeParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.decl_list()
            self.state = 85
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.decl()
                self.state = 88
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.variables()
                self.state = 95
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.implicit_var()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(ZCodeParser.VAR)
            self.state = 105
            self.match(ZCodeParser.ID)
            self.state = 106
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 107
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def NUMBER_list(self):
            return self.getToken(ZCodeParser.NUMBER_list, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.match(ZCodeParser.ID)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LP:
                    self.state = 111
                    self.match(ZCodeParser.LP)
                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZCodeParser.NUMBER_list:
                        self.state = 112
                        self.match(ZCodeParser.NUMBER_list)


                    self.state = 115
                    self.match(ZCodeParser.RP)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.match(ZCodeParser.ID)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.LP:
                    self.state = 120
                    self.match(ZCodeParser.LP)
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZCodeParser.NUMBER_list:
                        self.state = 121
                        self.match(ZCodeParser.NUMBER_list)


                    self.state = 124
                    self.match(ZCodeParser.RP)


                self.state = 127
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 128
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(ZCodeParser.DYNAMIC)
                self.state = 132
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(ZCodeParser.DYNAMIC)
                self.state = 134
                self.match(ZCodeParser.ID)
                self.state = 135
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.INT) | (1 << ZCodeParser.REAL) | (1 << ZCodeParser.STRING_LIT))) != 0):
                    self.state = 136
                    self.expression()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ZCodeParser.FUNC)
            self.state = 142
            self.match(ZCodeParser.ID)
            self.state = 143
            self.match(ZCodeParser.LB)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 144
                self.prameters_list()


            self.state = 147
            self.match(ZCodeParser.RB)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 148
                    self.ignore()


                self.state = 151
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 152
                    self.ignore()


                self.state = 155
                self.block_stmt()
                pass

            elif la_ == 3:
                self.state = 156
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def NUMBER_list(self):
            return self.getToken(ZCodeParser.NUMBER_list, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def prameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Prameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prameters_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrameters_list" ):
                return visitor.visitPrameters_list(self)
            else:
                return visitor.visitChildren(self)




    def prameters_list(self):

        localctx = ZCodeParser.Prameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_prameters_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 160
            self.match(ZCodeParser.ID)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LP:
                self.state = 161
                self.match(ZCodeParser.LP)
                self.state = 162
                self.match(ZCodeParser.NUMBER_list)
                self.state = 163
                self.match(ZCodeParser.RP)


            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.COMMA:
                self.state = 166
                self.match(ZCodeParser.COMMA)
                self.state = 167
                self.prameters_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.exp1()
                self.state = 171
                self.match(ZCodeParser.CONCAT)
                self.state = 172
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_EQUAL, 0)

        def GREAT(self):
            return self.getToken(ZCodeParser.GREAT, 0)

        def GREAT_EQUAL(self):
            return self.getToken(ZCodeParser.GREAT_EQUAL, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = ZCodeParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.exp2()
                self.state = 178
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.ASSIGN) | (1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.LESS_EQUAL) | (1 << ZCodeParser.GREAT) | (1 << ZCodeParser.GREAT_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.exp2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = ZCodeParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.exp3()
                self.state = 185
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.exp3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = ZCodeParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp3)
        self._la = 0 # Token type
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.exp4()
                self.state = 192
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                self.exp3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = ZCodeParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp4)
        self._la = 0 # Token type
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.exp5()
                self.state = 199
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.exp4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.exp5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp5)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(ZCodeParser.NOT)
                self.state = 206
                self.exp5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.ID, ZCodeParser.INT, ZCodeParser.REAL, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp6)
        self._la = 0 # Token type
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 211
                self.exp6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.LP, ZCodeParser.ID, ZCodeParser.INT, ZCodeParser.REAL, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Element_exprContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def exp8(self):
            return self.getTypedRuleContext(ZCodeParser.Exp8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp7)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 215
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 216
                    self.func_call()
                    pass


                self.state = 219
                self.element_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = ZCodeParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp8)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(ZCodeParser.LB)
                self.state = 225
                self.expression()
                self.state = 226
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literals_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def literals_list(self):
            return self.getTypedRuleContext(ZCodeParser.Literals_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literals_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals_list" ):
                return visitor.visitLiterals_list(self)
            else:
                return visitor.visitChildren(self)




    def literals_list(self):

        localctx = ZCodeParser.Literals_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literals_list)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.expression()
                self.state = 233
                self.match(ZCodeParser.COMMA)
                self.state = 234
                self.literals_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ZCodeParser.INT, 0)

        def REAL(self):
            return self.getToken(ZCodeParser.REAL, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def arr_literals(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_literalsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literals)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(ZCodeParser.INT)
                pass
            elif token in [ZCodeParser.REAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(ZCodeParser.REAL)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 243
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 244
                self.arr_literals()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_literalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def literals_list(self):
            return self.getTypedRuleContext(ZCodeParser.Literals_listContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_literals" ):
                return visitor.visitArr_literals(self)
            else:
                return visitor.visitChildren(self)




    def arr_literals(self):

        localctx = ZCodeParser.Arr_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arr_literals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ZCodeParser.LP)
            self.state = 248
            self.literals_list()
            self.state = 249
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def indx_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Indx_operatorContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




    def element_expr(self):

        localctx = ZCodeParser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(ZCodeParser.LP)
            self.state = 252
            self.indx_operator()
            self.state = 253
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indx_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def indx_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Indx_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indx_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndx_operator" ):
                return visitor.visitIndx_operator(self)
            else:
                return visitor.visitChildren(self)




    def indx_operator(self):

        localctx = ZCodeParser.Indx_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_indx_operator)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.expression()
                self.state = 256
                self.match(ZCodeParser.COMMA)
                self.state = 257
                self.indx_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_stmtContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Call_statementContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_statement)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 266
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 267
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 268
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 269
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 270
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def decl_stmt(self):

        localctx = ZCodeParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.variables()
            self.state = 274
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.lhs()
            self.state = 277
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 278
            self.expression()
            self.state = 279
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def element_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Element_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(ZCodeParser.ID)
                self.state = 282
                self.element_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(ZCodeParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def elseif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elseif_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.IF)
            self.state = 287
            self.match(ZCodeParser.LB)
            self.state = 288
            self.expression()
            self.state = 289
            self.match(ZCodeParser.RP)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 290
                self.ignore()


            self.state = 293
            self.stmt()
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 294
                self.elseif_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def elseif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elseif_statementContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elseif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_statement" ):
                return visitor.visitElseif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elseif_statement(self):

        localctx = ZCodeParser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elseif_statement)
        self._la = 0 # Token type
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(ZCodeParser.ELIF)
                self.state = 298
                self.match(ZCodeParser.LB)
                self.state = 299
                self.expression()
                self.state = 300
                self.match(ZCodeParser.RB)
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 301
                    self.ignore()


                self.state = 304
                self.stmt()
                self.state = 306
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 305
                    self.elseif_statement()


                pass
            elif token in [ZCodeParser.ELSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(ZCodeParser.ELSE)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 309
                    self.ignore()


                self.state = 312
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.FOR)
            self.state = 316
            self.match(ZCodeParser.ID)
            self.state = 317
            self.match(ZCodeParser.UNTIL)
            self.state = 318
            self.expression()
            self.state = 319
            self.match(ZCodeParser.BY)
            self.state = 320
            self.expression()
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 321
                self.ignore()


            self.state = 324
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(ZCodeParser.BREAK)
            self.state = 327
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.CONTINUE)
            self.state = 330
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(ZCodeParser.RETURN)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.INT) | (1 << ZCodeParser.REAL) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 333
                self.expression()


            self.state = 336
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.func_call()
            self.state = 339
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def indx_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Indx_operatorContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_func_call)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(ZCodeParser.ID)
                self.state = 342
                self.match(ZCodeParser.LB)
                self.state = 343
                self.indx_operator()
                self.state = 344
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(ZCodeParser.ID)
                self.state = 347
                self.match(ZCodeParser.LB)
                self.state = 348
                self.match(ZCodeParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(ZCodeParser.BEGIN)
            self.state = 352
            self.ignore()
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.ID))) != 0):
                self.state = 353
                self.stmt()


            self.state = 356
            self.match(ZCodeParser.END)
            self.state = 357
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.statement()
                self.state = 360
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 365
                self.match(ZCodeParser.NEWLINE)
                self.state = 368 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





