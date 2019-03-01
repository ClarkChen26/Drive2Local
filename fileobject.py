class FileObject:
    """
    A class to store information about file objects
    """
    
    def __init__(self, kind, id, title, mimeType, isStarred, isHidden, isTrashed, isRestricted, isViewed, createdDate, modifiedDate, ownerName, ownerEmail, isEditable, isCopyable):
        # The kind of object in Google Drive
        self.kind = kind
        # The id of the file
        self.id = id
        # The title of the file
        self.title = title
        # The MIME type of the file
        self.mimeType = mimeType
        # Whether or not the file is starred by the user
        self.isStarred = isStarred
        # Whether or not the file is marked hidden
        self.isHidden = isHidden
        # Whether or not the file has been trashed
        self.isTrashed = isTrashed
        # Whether or not the file is marked as restricted
        self.isRestricted = isRestricted
        # Whether or not the file has been viewed
        self.isViewed = isViewed
        # The creation date of the file in yyy-mm-ddTHH:MM:SSSSSZ
        self.createdDate = createdDate
        # The last modification date of the file in yyy-mm-ddTHH:MM:SSSSSZ
        self.modifiedDate = modifiedDate
        # The owner of the file's name
        self.ownerName = ownerName
        # The owner of the file's email
        self.ownerEmail = ownerEmail
        # Whether or not the file is editable by the user
        self.isEditable = isEditable
        # Whether or not the file is copyable by the user
        self.isCopyable = isCopyable