thread:
	run(Threads_running):
	目前正在執行中的連線數
	The number of threads that are not sleeping

	con(Threads_connected):
	日前已開啟的連線數=show processlist
	The number of currently open connections.

	cac(Threads_cached):
	MySQL管理的線程池中還有多少個thread可以重複被利用
	The number of threads in the thread cache.

	cre(Threads_created):
	為連線時所開啟的thread數，如此數值過大，需增加thread_cache_size。
	The number of threads created to handle connections.
	If Threads_created is big, you may want to increase the thread_cache_size value.
	The cache miss rate can be calculated as Threads_created/Connections(The number of connection attempts (successful or not) to the MySQL server).

innodb lock:
	cu(Innodb_row_lock_current_waits)
	目前正在等待獲得row lock的數量
	The number of row locks currently being waited for by operations on InnoDB tables.

	wa(Innodb_row_lock_waits)
	目前產生多少次的row lock等待
	The number of times operations on InnoDB tables had to wait for a row lock.

	ti(Innodb_row_lock_time)
	目前row lock等待的時間(avg_wait : Innodb_row_lock_time/Innodb_row_lock_waits=Innodb_row_lock_time_avg)
	The total time spent in acquiring row locks for InnoDB tables, in milliseconds.

mysql:
	i(Com_insert)
	目前insert statement被執行的次數(包含錯誤、失敗、rollback)

	u(Com_update)
	目前update statement被執行的次數(包含錯誤、失敗、rollback)

	d(Com_delete)
	目前delete statement被執行的次數(包含錯誤、失敗、rollback)

	s(Com_select)
	目前select statement被執行的次數(包含錯誤、失敗、rollback)

	c(Com_commit)
	commit次數

	r(Com_rollback)
	rollback次數

	rh(rollback hit)
	rollback比率:rollback/commit

tmp
tmp_table_size
The maximum size of internal in-memory temporary tables. This variable does not apply to user-created MEMORY tables.

max_heap_table_size
This variable sets the maximum size to which user-created MEMORY tables are permitted to grow. The value of the variable is used to calculate MEMORY table MAX_ROWS values. 
