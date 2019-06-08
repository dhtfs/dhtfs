#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class FileSystemModel(object):
    PASTIS = 0
    BASIC = 1
    SNAPSHOT = 2

    _VALUES_TO_NAMES = {
        0: "PASTIS",
        1: "BASIC",
        2: "SNAPSHOT",
    }

    _NAMES_TO_VALUES = {
        "PASTIS": 0,
        "BASIC": 1,
        "SNAPSHOT": 2,
    }


class InodeType(object):
    FILE = 0
    DIRECTORY = 1
    SYMLINK = 2

    _VALUES_TO_NAMES = {
        0: "FILE",
        1: "DIRECTORY",
        2: "SYMLINK",
    }

    _NAMES_TO_VALUES = {
        "FILE": 0,
        "DIRECTORY": 1,
        "SYMLINK": 2,
    }


class InodeFlags(object):
    EXECUTABLE = 1

    _VALUES_TO_NAMES = {
        1: "EXECUTABLE",
    }

    _NAMES_TO_VALUES = {
        "EXECUTABLE": 1,
    }


class DirEntryDiffType(object):
    ADD = 0
    REMOVE = 1

    _VALUES_TO_NAMES = {
        0: "ADD",
        1: "REMOVE",
    }

    _NAMES_TO_VALUES = {
        "ADD": 0,
        "REMOVE": 1,
    }


class FileSystem(object):
    """
    Attributes:
     - name
     - block_size
     - root
     - inception
     - model
    """


    def __init__(self, name=None, block_size=None, root=None, inception=None, model=1,):
        self.name = name
        self.block_size = block_size
        self.root = root
        self.inception = inception
        self.model = model

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.block_size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.root = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.inception = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.model = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FileSystem')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.block_size is not None:
            oprot.writeFieldBegin('block_size', TType.I32, 2)
            oprot.writeI32(self.block_size)
            oprot.writeFieldEnd()
        if self.root is not None:
            oprot.writeFieldBegin('root', TType.I64, 3)
            oprot.writeI64(self.root)
            oprot.writeFieldEnd()
        if self.inception is not None:
            oprot.writeFieldBegin('inception', TType.I64, 4)
            oprot.writeI64(self.inception)
            oprot.writeFieldEnd()
        if self.model is not None:
            oprot.writeFieldBegin('model', TType.I32, 5)
            oprot.writeI32(self.model)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        if self.block_size is None:
            raise TProtocolException(message='Required field block_size is unset!')
        if self.root is None:
            raise TProtocolException(message='Required field root is unset!')
        if self.inception is None:
            raise TProtocolException(message='Required field inception is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FileData(object):
    """
    Attributes:
     - size
     - blocks
     - indirect
    """


    def __init__(self, size=None, blocks=None, indirect=None,):
        self.size = size
        self.blocks = blocks
        self.indirect = indirect

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.size = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.blocks = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readBinary()
                        self.blocks.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.indirect = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readBinary()
                        self.indirect.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FileData')
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I64, 1)
            oprot.writeI64(self.size)
            oprot.writeFieldEnd()
        if self.blocks is not None:
            oprot.writeFieldBegin('blocks', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.blocks))
            for iter12 in self.blocks:
                oprot.writeBinary(iter12)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.indirect is not None:
            oprot.writeFieldBegin('indirect', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.indirect))
            for iter13 in self.indirect:
                oprot.writeBinary(iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.size is None:
            raise TProtocolException(message='Required field size is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class FileDataIndirect(object):
    """
    Attributes:
     - blocks
     - valid
    """


    def __init__(self, blocks=None, valid=True,):
        self.blocks = blocks
        self.valid = valid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.blocks = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = iprot.readBinary()
                        self.blocks.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.valid = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('FileDataIndirect')
        if self.blocks is not None:
            oprot.writeFieldBegin('blocks', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.blocks))
            for iter20 in self.blocks:
                oprot.writeBinary(iter20)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.valid is not None:
            oprot.writeFieldBegin('valid', TType.BOOL, 2)
            oprot.writeBool(self.valid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.blocks is None:
            raise TProtocolException(message='Required field blocks is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DirEntry(object):
    """
    Attributes:
     - inumber
     - type
    """


    def __init__(self, inumber=None, type=None,):
        self.inumber = inumber
        self.type = type

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.inumber = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('DirEntry')
        if self.inumber is not None:
            oprot.writeFieldBegin('inumber', TType.I64, 1)
            oprot.writeI64(self.inumber)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.inumber is None:
            raise TProtocolException(message='Required field inumber is unset!')
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DirEntryDiff(object):
    """
    Attributes:
     - diff_type
     - entry
     - mtime
     - name
    """


    def __init__(self, diff_type=None, entry=None, mtime=None, name=None,):
        self.diff_type = diff_type
        self.entry = entry
        self.mtime = mtime
        self.name = name

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.diff_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.entry = DirEntry()
                    self.entry.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.mtime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('DirEntryDiff')
        if self.diff_type is not None:
            oprot.writeFieldBegin('diff_type', TType.I32, 1)
            oprot.writeI32(self.diff_type)
            oprot.writeFieldEnd()
        if self.entry is not None:
            oprot.writeFieldBegin('entry', TType.STRUCT, 2)
            self.entry.write(oprot)
            oprot.writeFieldEnd()
        if self.mtime is not None:
            oprot.writeFieldBegin('mtime', TType.I64, 3)
            oprot.writeI64(self.mtime)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 4)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.diff_type is None:
            raise TProtocolException(message='Required field diff_type is unset!')
        if self.entry is None:
            raise TProtocolException(message='Required field entry is unset!')
        if self.mtime is None:
            raise TProtocolException(message='Required field mtime is unset!')
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DirData(object):
    """
    Attributes:
     - entries
     - count
     - indirect
    """


    def __init__(self, entries=None, count=None, indirect=None,):
        self.entries = entries
        self.count = count
        self.indirect = indirect

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.MAP:
                    self.entries = {}
                    (_ktype22, _vtype23, _size21) = iprot.readMapBegin()
                    for _i25 in range(_size21):
                        _key26 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val27 = DirEntry()
                        _val27.read(iprot)
                        self.entries[_key26] = _val27
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.count = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.indirect = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('DirData')
        if self.entries is not None:
            oprot.writeFieldBegin('entries', TType.MAP, 1)
            oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.entries))
            for kiter28, viter29 in self.entries.items():
                oprot.writeString(kiter28.encode('utf-8') if sys.version_info[0] == 2 else kiter28)
                viter29.write(oprot)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.count is not None:
            oprot.writeFieldBegin('count', TType.I64, 2)
            oprot.writeI64(self.count)
            oprot.writeFieldEnd()
        if self.indirect is not None:
            oprot.writeFieldBegin('indirect', TType.STRING, 3)
            oprot.writeBinary(self.indirect)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class DirDataIndirect(object):
    """
    Attributes:
     - entries
     - valid
    """


    def __init__(self, entries=None, valid=True,):
        self.entries = entries
        self.valid = valid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.MAP:
                    self.entries = {}
                    (_ktype31, _vtype32, _size30) = iprot.readMapBegin()
                    for _i34 in range(_size30):
                        _key35 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val36 = DirEntry()
                        _val36.read(iprot)
                        self.entries[_key35] = _val36
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.valid = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('DirDataIndirect')
        if self.entries is not None:
            oprot.writeFieldBegin('entries', TType.MAP, 1)
            oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.entries))
            for kiter37, viter38 in self.entries.items():
                oprot.writeString(kiter37.encode('utf-8') if sys.version_info[0] == 2 else kiter37)
                viter38.write(oprot)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.valid is not None:
            oprot.writeFieldBegin('valid', TType.BOOL, 2)
            oprot.writeBool(self.valid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SymLinkData(object):
    """
    Attributes:
     - target
    """


    def __init__(self, target=None,):
        self.target = target

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.target = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('SymLinkData')
        if self.target is not None:
            oprot.writeFieldBegin('target', TType.STRING, 1)
            oprot.writeString(self.target.encode('utf-8') if sys.version_info[0] == 2 else self.target)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.target is None:
            raise TProtocolException(message='Required field target is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Inode(object):
    """
    Attributes:
     - id
     - inumber
     - type
     - mtime
     - flags
     - file_data
     - directory_data
     - symlink_data
    """


    def __init__(self, id=None, inumber=None, type=None, mtime=None, flags=0, file_data=None, directory_data=None, symlink_data=None,):
        self.id = id
        self.inumber = inumber
        self.type = type
        self.mtime = mtime
        self.flags = flags
        self.file_data = file_data
        self.directory_data = directory_data
        self.symlink_data = symlink_data

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.inumber = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.mtime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.flags = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.file_data = FileData()
                    self.file_data.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.directory_data = DirData()
                    self.directory_data.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.symlink_data = SymLinkData()
                    self.symlink_data.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Inode')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.I64, 1)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        if self.inumber is not None:
            oprot.writeFieldBegin('inumber', TType.I64, 2)
            oprot.writeI64(self.inumber)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.mtime is not None:
            oprot.writeFieldBegin('mtime', TType.I64, 4)
            oprot.writeI64(self.mtime)
            oprot.writeFieldEnd()
        if self.flags is not None:
            oprot.writeFieldBegin('flags', TType.I32, 5)
            oprot.writeI32(self.flags)
            oprot.writeFieldEnd()
        if self.file_data is not None:
            oprot.writeFieldBegin('file_data', TType.STRUCT, 6)
            self.file_data.write(oprot)
            oprot.writeFieldEnd()
        if self.directory_data is not None:
            oprot.writeFieldBegin('directory_data', TType.STRUCT, 7)
            self.directory_data.write(oprot)
            oprot.writeFieldEnd()
        if self.symlink_data is not None:
            oprot.writeFieldBegin('symlink_data', TType.STRUCT, 8)
            self.symlink_data.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.inumber is None:
            raise TProtocolException(message='Required field inumber is unset!')
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        if self.mtime is None:
            raise TProtocolException(message='Required field mtime is unset!')
        if self.flags is None:
            raise TProtocolException(message='Required field flags is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(FileSystem)
FileSystem.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    (2, TType.I32, 'block_size', None, None, ),  # 2
    (3, TType.I64, 'root', None, None, ),  # 3
    (4, TType.I64, 'inception', None, None, ),  # 4
    (5, TType.I32, 'model', None, 1, ),  # 5
)
all_structs.append(FileData)
FileData.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'size', None, None, ),  # 1
    (2, TType.LIST, 'blocks', (TType.STRING, 'BINARY', False), None, ),  # 2
    (3, TType.LIST, 'indirect', (TType.STRING, 'BINARY', False), None, ),  # 3
)
all_structs.append(FileDataIndirect)
FileDataIndirect.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'blocks', (TType.STRING, 'BINARY', False), None, ),  # 1
    (2, TType.BOOL, 'valid', None, True, ),  # 2
)
all_structs.append(DirEntry)
DirEntry.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'inumber', None, None, ),  # 1
    (2, TType.I32, 'type', None, None, ),  # 2
)
all_structs.append(DirEntryDiff)
DirEntryDiff.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'diff_type', None, None, ),  # 1
    (2, TType.STRUCT, 'entry', [DirEntry, None], None, ),  # 2
    (3, TType.I64, 'mtime', None, None, ),  # 3
    (4, TType.STRING, 'name', 'UTF8', None, ),  # 4
)
all_structs.append(DirData)
DirData.thrift_spec = (
    None,  # 0
    (1, TType.MAP, 'entries', (TType.STRING, 'UTF8', TType.STRUCT, [DirEntry, None], False), None, ),  # 1
    (2, TType.I64, 'count', None, None, ),  # 2
    (3, TType.STRING, 'indirect', 'BINARY', None, ),  # 3
)
all_structs.append(DirDataIndirect)
DirDataIndirect.thrift_spec = (
    None,  # 0
    (1, TType.MAP, 'entries', (TType.STRING, 'UTF8', TType.STRUCT, [DirEntry, None], False), None, ),  # 1
    (2, TType.BOOL, 'valid', None, True, ),  # 2
)
all_structs.append(SymLinkData)
SymLinkData.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'target', 'UTF8', None, ),  # 1
)
all_structs.append(Inode)
Inode.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'id', None, None, ),  # 1
    (2, TType.I64, 'inumber', None, None, ),  # 2
    (3, TType.I32, 'type', None, None, ),  # 3
    (4, TType.I64, 'mtime', None, None, ),  # 4
    (5, TType.I32, 'flags', None, 0, ),  # 5
    (6, TType.STRUCT, 'file_data', [FileData, None], None, ),  # 6
    (7, TType.STRUCT, 'directory_data', [DirData, None], None, ),  # 7
    (8, TType.STRUCT, 'symlink_data', [SymLinkData, None], None, ),  # 8
)
fix_spec(all_structs)
del all_structs
