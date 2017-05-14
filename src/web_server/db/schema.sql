drop table if exists Metrics;

create table Metrics (
	
	Id integer primary key autoincrement,
	
	Timestamp datetime not null,
	
	LeftImageFilePath varchar(4096),
	LeftImage blob,
	
	RightImageFilePath varchar(4096),
	RightImage blob,
	
	CompositeImage blob,
	CompositeImageFilePath varchar(4096),

	Note text
);