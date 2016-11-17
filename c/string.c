void remove_substring(char* s, const char* toremove){
	while((s = strstr(s, toremove)))
		memmove(s, s+strlen(toremove), 1 + strlen(s + strlen(toremove)));
}
