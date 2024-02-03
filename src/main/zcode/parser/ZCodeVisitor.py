# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prameters_list.
    def visitPrameters_list(self, ctx:ZCodeParser.Prameters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp1.
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp2.
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp3.
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp4.
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp5.
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp6.
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp7.
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp8.
    def visitExp8(self, ctx:ZCodeParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literals_list.
    def visitLiterals_list(self, ctx:ZCodeParser.Literals_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_literals.
    def visitArr_literals(self, ctx:ZCodeParser.Arr_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#element_expr.
    def visitElement_expr(self, ctx:ZCodeParser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indx_operator.
    def visitIndx_operator(self, ctx:ZCodeParser.Indx_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_stmt.
    def visitDecl_stmt(self, ctx:ZCodeParser.Decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseif_statement.
    def visitElseif_statement(self, ctx:ZCodeParser.Elseif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_statement.
    def visitCall_statement(self, ctx:ZCodeParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call.
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)



del ZCodeParser