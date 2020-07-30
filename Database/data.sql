
INSERT INTO `geektextdb`.`author`
(`firstName`, `lastName`, `biography`, `publisher`)
VALUES
('Stephen', 'King', 'American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels.', 'Scribner'),
('George', 'Orwell', 'English novelist, essayist, journalist and critic.[2] His work is characterised by lucid prose, biting social criticism, opposition to totalitarianism, and outspoken support of democratic socialism.', 'Secker & Warburg'),
('J. K.', 'Rowling', 'British author, screenwriter, producer, and philanthropist', 'Bloomsbury'),
('Mark', 'Twain', 'American writer, humorist, entrepreneur, publisher, and lecturer', 'American Publishing Company'),
('William', 'Shakespeare', ' English playwright, poet, and actor, widely regarded as the greatest writer in the English language and the worlds greatest dramatist', 'Edward Blount and William and Isaac Jaggard');

INSERT INTO `geektextdb`.`book`
(`isbn`, `idAuthor`, `bookName`, `description`, `price`, `genre`, `publisher`, `yearPublished`)
VALUES
('1594130000', '3', 'Harry Potter And The Sorcerers Stone', 'The first novel in the Harry Potter series and Rowlings debut novel', '13.95', 'Fantasy', 'Bloomsbury', '1997'),
('0736648046', '3', 'Harry Potter and the Chamber of Secrets', 'a fantasy novel written by British author J. K. Rowling and the second novel in the Harry Potter series', '13.95', 'Fantasy', 'Bloomsbury', '1998'),
('1443434973', '2', '1984', 'a dystopian novel by English novelist George Orwell. It was published on 8 June 1949 by Secker & Warburg as Orwells\'s ninth and final book completed in his lifetime', '13.94', 'Dystopian', 'Secker & Warburg', '1949'),
('1501142976', '1', 'It: A Novel', 'Stephen King’s terrifyin novel about seven adults who return to their hometown to confront a nightmare they had first stumbled on as teenagers…an evil without a name: It.', '8.93', 'Horror', 'Scribner', '1986'),
('0307743659', '1', 'The Shining', 'Before Doctor Sleep, there was The Shining, a classic of modern American horror from the undisputed master, Stephen King.', '6.70', 'Horror', 'Anchor', '1977'),
('1501180983', '1', 'The Outsider: A Novel', 'Evil has many faces…maybe even yours in this #1 New York Times bestseller from master storyteller Stephen King.', '11.68', 'Horror', 'Scribner', '2018');

INSERT INTO `geektextdb`.`user`
(`username`, `password`, `name`, `address`)
VALUES
('guillermocasal', '1234', 'Guillermo Casal', '123 Test St'),
('booklover', '1234', 'Test User', '124 Test St');

UPDATE rating
SET rating=4
WHERE user_iduser=3;
