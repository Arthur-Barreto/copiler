; constantes
SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1
True equ 1
False equ 0

segment .data

formatin: db "%d", 0
formatout: db "%d", 10, 0 ; newline, nul terminator
scanint: times 4 db 0 ; 32-bits integer = 4 bytes

segment .bss  ; variaveis
    res RESB 1

section .text
    global main
    extern scanf
    extern printf
    extern fflush
    extern stdout

; subrotinas if/while

binop_je:
    JE binop_true
    JMP binop_false

binop_jg:
    JG binop_true
    JMP binop_false

binop_jl:
    JL binop_true
    JMP binop_false

binop_false:
    MOV EAX, False  
    JMP binop_exit
binop_true:
    MOV EAX, True
binop_exit:
    RET

main:

    PUSH EBP ; guarda o base pointer
    MOV EBP, ESP ; estabelece um novo base pointer

; codigo gerado pelo compilador abaixo
   PUSH DWORD 0
   ;;; int_val ;;;
   MOV EAX, 10
   ;;; fim int_val ;;;
   ;;; assignment ;;;
   MOV [EBP-4], EAX
   ;;; fim assignment ;;;
   ;;; while ;;;
   LOOP_14:
   ;;; int_val ;;;
   MOV EAX, 0
   ;;; fim int_val ;;;
   PUSH EAX
   ;;; identifier ;;;
   MOV EAX, [EBP-4]
   ;;; fim identifier ;;;
   POP EBX
   CMP EAX, EBX
   CALL binop_jg
   CMP EAX, False
   JE EXIT_14
   ;;; identifier ;;;
   MOV EAX, [EBP-4]
   ;;; fim identifier ;;;
   ;;; print ;;;;
   PUSH EAX
   PUSH formatout
   CALL printf
   ADD ESP, 8
   ;;; fim do print ;;;;
   ;;; int_val ;;;
   MOV EAX, 1
   ;;; fim int_val ;;;
   PUSH EAX
   ;;; identifier ;;;
   MOV EAX, [EBP-4]
   ;;; fim identifier ;;;
   POP EBX
   SUB EAX, EBX
   ;;; assignment ;;;
   MOV [EBP-4], EAX
   ;;; fim assignment ;;;
   JMP LOOP_14
   EXIT_14:
   ;;; fim while ;;;
; interrupcao de saida (default)

    PUSH DWORD [stdout]
    CALL fflush
    ADD ESP, 4

    MOV ESP, EBP
    POP EBP

    MOV EAX, 1
    XOR EBX, EBX
    INT 0x80