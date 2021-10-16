from enum import Enum

class JVMOpcodes(Enum):
    aaload = 0x32
    aastore = 0x53
    aconst_null = 0x1
    aload = 0x19
    aload_0 = 0x2a
    aload_1 = 0x2b
    aload_2 = 0x2c
    aload_3 = 0x2d
    anewarray = 0xbd
    areturn = 0xb0
    arraylength = 190 
    astore = 58 
    astore_0 = 75 
    astore_1 = 76 
    astore_2 = 77 
    astore_3 = 78 
    athrow = 191 
    baload = 51 
    bastore = 84 
    bipush = 16 
    caload = 52 
    castore = 85 
    checkcast = 192 
    d2f = 144 
    d2i = 142 
    d2l = 143 
    dadd = 99 
    daload = 49 
    dastore = 82 
    dcmpg = 152 
    dcmpl = 151 
    dconst_0 = 14 
    dconst_1 = 15 
    ddiv = 111 
    dload = 24 
    dload_0 = 38 
    dload_1 = 39 
    dload_2 = 40 
    dload_3 = 41 
    dmul = 107 
    dneg = 119 
    drem = 115 
    dreturn = 175 
    dstore = 57 
    dstore_0 = 71 
    dstore_1 = 72 
    dstore_2 = 73 
    dstore_3 = 74 
    dsub = 103 
    dup = 89 
    dup_x1 = 90 
    dup_x2 = 91 
    dup2 = 92 
    dup2_x1 = 93 
    dup2_x2 = 94 
    f2d = 141 
    f2i = 139 
    f2l = 140 
    fadd = 98 
    faload = 48 
    fastore = 81 
    fcmpg = 150 
    fcmpl = 149 
    fconst_0 = 11 
    fconst_1 = 12 
    fconst_2 = 13 
    fdiv = 110 
    fload = 23 
    fload_0 = 34 
    fload_1 = 35 
    fload_2 = 36 
    fload_3 = 37 
    fmul = 106 
    fneg = 118 
    frem = 114 
    freturn = 174 
    fstore = 56 
    fstore_0 = 67 
    fstore_1 = 68 
    fstore_2 = 69 
    fstore_3 = 70 
    fsub = 102 
    getfield = 180 
    getstatic = 178 
    goto = 167 
    goto_w = 200 
    i2b = 145 
    i2c = 146 
    i2d = 135 
    i2f = 134 
    i2l = 133 
    i2s = 147 
    iadd = 96 
    iaload = 46 
    iand = 126 
    iastore = 79 
    iconst_m1 = 2 
    iconst_0 = 3 
    iconst_1 = 4 
    iconst_2 = 5 
    iconst_3 = 6 
    iconst_4 = 7 
    iconst_5 = 8 
    idiv = 108 
    if_acmpeq = 165 
    if_acmpne = 166 
    if_icmpeq = 159 
    if_icmpne = 160 
    if_icmplt = 161 
    if_icmpge = 162 
    if_icmpgt = 163 
    if_icmple = 164 
    ifeq = 153 
    ifne = 154 
    iflt = 155 
    ifge = 156 
    ifgt = 157 
    ifle = 158 
    ifnonnull = 199 
    ifnull = 198 
    iinc = 132 
    iload = 21 
    iload_0 = 26 
    iload_1 = 27 
    iload_2 = 28 
    iload_3 = 29 
    imul = 104 
    ineg = 116 
    instanceof = 193 
    invokedynamic = 186 
    invokeinterface = 185 
    invokespecial = 183 
    invokestatic = 184 
    invokevirtual = 182 
    ior = 128 
    irem = 112 
    ireturn = 172 
    ishl = 120 
    ishr = 122 
    istore = 54 
    istore_0 = 59 
    istore_1 = 60 
    istore_2 = 61 
    istore_3 = 62 
    isub = 100 
    iushr = 124 
    ixor = 130 
    jsr = 168 
    jsr_w = 201 
    l2d = 138 
    l2f = 137 
    l2i = 136 
    ladd = 97 
    laload = 47 
    land = 127 
    lastore = 80 
    lcmp = 148 
    lconst_0 = 9 
    lconst_1 = 10 
    ldc = 18 
    ldc_w = 19 
    ldc2_w = 20 
    ldiv = 109 
    lload = 22 
    lload_0 = 30 
    lload_1 = 31 
    lload_2 = 32 
    lload_3 = 33 
    lmul = 105 
    lneg = 117 
    lookupswitch = 171 
    lor = 129 
    lrem = 113 
    lreturn = 173 
    lshl = 121 
    lshr = 123 
    lstore = 55 
    lstore_0 = 63 
    lstore_1 = 64 
    lstore_2 = 65 
    lstore_3 = 66 
    lsub = 101 
    lushr = 125 
    lxor = 131 
    monitorenter = 194 
    monitorexit = 195 
    multianewarray = 197 
    new = 187 
    newarray = 188 
    nop = 0 
    pop = 87 
    pop2 = 88 
    putfield = 181 
    putstatic = 179 
    ret = 169 
    return_ = 177 
    saload = 53 
    sastore = 86 
    sipush = 17 
    swap = 95 
    tableswitch = 170 
    wide = 196 

def main():
    print("Hello, World!")
